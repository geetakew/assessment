import pandas as pd


class DiceGameTransformer:
    """Transforms raw game data into dimensional and fact tables for analysis."""

    def __init__(self, data):
        """Initialize with raw data dictionary."""
        self.data = data

    def transform_dim_user(self):
        """Transform user dimension data."""
        return self.data["user"][["user_id", "ip_address", "social_media_handle", "email"]]

    def transform_dim_user_registration(self):
        """Transform user registration dimension data."""
        return self.data["user_registration"]

    def transform_dim_plan(self):
        return self.data["plan"]

    def transform_dim_payment_frequency(self):
        return self.data["plan_payment_frequency"]

    def transform_dim_channel(self):
        return self.data["channel_code"]

    def transform_fact_play_sessions(self):
        """Transform fact table of play sessions with date keys."""
        sessions = self.data["user_play_session"]
        sessions["start_time"] = pd.to_datetime(sessions["start_datetime"])
        sessions["date_key"] = sessions["start_time"].dt.strftime('%Y%m%d')
        return sessions[["play_session_id", "user_id", "date_key", "start_datetime", "end_datetime", "channel_code", "status_code", "total_score"]]

    def transform_fact_user_payments(self):
        """Transform fact table of user payments with merged registration and payment info."""
        reg = self.data["user_registration"]
        plan = self.data["user_plan"]
        pay = self.data["user_payment_detail"]
        full = plan.merge(reg, on="user_registration_id", how="left").merge(pay, on="payment_detail_id", how="left")
        return full[["payment_detail_id", "user_id", "plan_id", "start_date", "end_date", "payment_method_code"]]

    def transform_dim_status_code(self):
        status = self.data["status_code"]
        # Rename columns if needed for consistency
        status = status.rename(columns={
            "play_session_status_code": "status_code",
            "english_description": "status_desc_en",
            "french_description": "status_desc_fr"
        })
        return status

    def transform_all(self):
        """Run all transformations and return a dictionary of transformed DataFrames."""
        return {
            "dim_user": self.transform_dim_user(),
            "dim_user_registration": self.transform_dim_user_registration(),
            "dim_plan": self.transform_dim_plan(),
            "dim_payment_frequency": self.transform_dim_payment_frequency(),
            "dim_channel": self.transform_dim_channel(),
            "dim_status_code": self.transform_dim_status_code(),
            "fact_play_sessions": self.transform_fact_play_sessions(),
            "fact_user_payments": self.transform_fact_user_payments()
        }
