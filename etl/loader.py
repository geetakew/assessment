import pandas as pd
import os
import yaml

# Load config once
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

DATA_DIR = os.path.join(BASE_DIR, config["data_dir"])
OUTPUT_DIR = os.path.join(BASE_DIR, config.get("output_dir", "."))


def load_csv(name):
    """Load a CSV file by name from the configured data directory into a DataFrame."""
    path = os.path.join(DATA_DIR, f"{name}.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)


def load_all_sources():
    """Load all configured CSV source files into a dictionary of DataFrames."""
    data = {}
    for file_name in config["files"]:
        key = file_name
        data[key] = load_csv(file_name)
    return data


def save_all_outputs(dataframes, output_dir=OUTPUT_DIR):
    """Save multiple DataFrames as CSV files into the specified output directory."""
    os.makedirs(output_dir, exist_ok=True)
    for name, df in dataframes.items():
        df.to_csv(os.path.join(output_dir, f"{name}.csv"), index=False)
