import pandas as pd
import pytest
from etl.insights import generate_insights


def test_generate_insights_prints(monkeypatch, capsys):
    fact_play_sessions = pd.DataFrame({
        "play_session_id": [1, 2],
        "channel_code": ["BROWSER", "MOBILE"],
        "status_code": ["COMPLETED", "ABORTED"],
        "total_score": [100, 200]
    })

    fact_user_payments = pd.DataFrame({
        "payment_detail_id": [1],
        "user_id": [1],
        "plan_id": [1],
        "start_date": ["2024-01-01"],
        "end_date": ["2024-12-31"],
        "payment_method_code": ["CARD"]
    })

    dim_plan = pd.DataFrame({
        "plan_id": [1, 2],  # <-- Added this column
        "payment_frequency_code": ["MONTHLY", "ONETIME"],
        "cost_amount": [1.99, 14.99]
    })

    transformed_data = {
        "fact_play_sessions": fact_play_sessions,
        "dim_plan": dim_plan,
        "fact_user_payments": fact_user_payments
    }

    generate_insights(transformed_data)

    captured = capsys.readouterr()
    assert "Sessions by Channel:" in captured.out
    assert "Payment Type Counts:" in captured.out  # <-- updated this line
    assert "Gross Revenue" in captured.out
