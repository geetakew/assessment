import pandas as pd
import pytest
from etl.transformer import DiceGameTransformer


@pytest.fixture
def sample_data():
    return {
        "user": pd.DataFrame({"user_id": [1], "ip_address": ["127.0.0.1"], "social_media_handle": ["user1"], "email": ["test@example.com"]}),
        "user_registration": pd.DataFrame({"user_registration_id": [1], "user_id": [1], "username": ["user1"], "email": ["test@example.com"], "first_name": ["Test"], "last_name": ["User"]}),
        "plan": pd.DataFrame({"plan_id": [1], "payment_frequency_code": ["MONTHLY"], "cost_amount": [1.99]}),
        "plan_payment_frequency": pd.DataFrame({"payment_frequency_code": ["MONTHLY"], "english_description": ["Monthly"], "french_description": ["Mensuel"]}),
        "channel_code": pd.DataFrame({"play_session_channel_code": ["BROWSER"], "english_description": ["Browser"], "french_description": ["Navigateur"]}),
        "status_code": pd.DataFrame({
            "play_session_status_code": ["COMPLETED"],
            "english_description": ["Session completed"],
            "french_description": ["Session terminée"]
        }),
        "user_play_session": pd.DataFrame({
            "play_session_id": [1],
            "user_id": [1],
            "start_datetime": ["2024-01-01T10:00:00"],
            "end_datetime": ["2024-01-01T11:00:00"],
            "channel_code": ["BROWSER"],
            "status_code": ["COMPLETED"],
            "total_score": [100]
        }),
        "user_plan": pd.DataFrame({"user_registration_id": [1], "payment_detail_id": [1], "plan_id": [1], "start_date": ["2024-01-01"], "end_date": ["2024-12-31"]}),
        "user_payment_detail": pd.DataFrame({"payment_detail_id": [1], "payment_method_code": ["CARD"], "payment_method_value": ["1234"], "payment_method_expiry": ["2025-01"]})
    }


def test_transform_dim_status_code(sample_data):
    transformer = DiceGameTransformer(sample_data)
    dim_status_code = transformer.transform_dim_status_code()
    assert "status_code" in dim_status_code.columns
    assert "status_desc_en" in dim_status_code.columns
    assert dim_status_code.iloc[0]["status_code"] == "COMPLETED"


def test_transform_fact_play_sessions(sample_data):
    transformer = DiceGameTransformer(sample_data)
    fact_sessions = transformer.transform_fact_play_sessions()
    # Check that expected columns are present
    expected_columns = [
        "play_session_id", "user_id", "date_key", "start_datetime",
        "end_datetime", "channel_code", "status_code", "total_score"
    ]
    assert all(col in fact_sessions.columns for col in expected_columns)
    # Check that the date_key is correct
    assert fact_sessions.iloc[0]["date_key"] == "20240101"


def test_transform_all(sample_data):
    transformer = DiceGameTransformer(sample_data)
    all_transforms = transformer.transform_all()
    expected_keys = {
        "dim_user", "dim_user_registration", "dim_plan", "dim_payment_frequency",
        "dim_channel", "dim_status_code", "fact_play_sessions", "fact_user_payments"
    }
    assert expected_keys == set(all_transforms.keys())
