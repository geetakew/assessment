import os
import pandas as pd
import pytest
from etl.loader import load_csv, load_all_sources, save_all_outputs


# Create a temporary data folder structure
@pytest.fixture
def tmp_data_dir(tmp_path):
    data_dir = tmp_path / "Dice_Game_Datasets"
    data_dir.mkdir()
    # Create a simple CSV file
    (data_dir / "user.csv").write_text("user_id,ip_address,email\n1,127.0.0.1,test@example.com\n")
    (data_dir / "status_code.csv").write_text("play_session_status_code,english_description,french_description\nCOMPLETED,Session completed,Session terminée\n")
    return data_dir


def test_load_csv_success(tmp_data_dir, monkeypatch):
    monkeypatch.setattr("etl.loader.DATA_DIR", str(tmp_data_dir))
    df = load_csv("user")
    assert not df.empty
    assert "user_id" in df.columns


def test_load_csv_missing_file(tmp_data_dir, monkeypatch):
    monkeypatch.setattr("etl.loader.DATA_DIR", str(tmp_data_dir))
    with pytest.raises(FileNotFoundError):
        load_csv("nonexistent_file")


def test_load_all_sources(tmp_data_dir, monkeypatch):
    # Write all required dummy CSVs for load_all_sources
    filenames = [
        "user", "user_registration", "user_play_session",
        "user_plan", "user_payment_detail", "plan",
        "plan_payment_frequency", "channel_code", "status_code"
    ]
    for name in filenames:
        (tmp_data_dir / f"{name}.csv").write_text("col1\nvalue")
    monkeypatch.setattr("etl.loader.DATA_DIR", str(tmp_data_dir))
    data = load_all_sources()
    assert set(data.keys()) == set(filenames)


def test_save_all_outputs(tmp_path):
    data = {
        "sample": pd.DataFrame({"col1": [1, 2, 3]})
    }
    save_all_outputs(dataframes=data, output_dir=tmp_path)
    output_file = tmp_path / "sample.csv"
    assert output_file.exists()
    saved_df = pd.read_csv(output_file)
    assert not saved_df.empty
    assert "col1" in saved_df.columns
