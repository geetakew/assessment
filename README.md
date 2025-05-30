# Dice Game ETL and Insights Pipeline

This project implements an ETL (Extract, Transform, Load) pipeline and generates insights on a dice game dataset. It includes data loading, transformation, and insights generation modules with unit tests.

---

## Features

- Load raw CSV datasets into pandas DataFrames
- Transform raw data into analytical formats
- Generate game insights from transformed data
- Save output datasets as CSV files
- Unit tests for all modules using `pytest`

---

Configuration: config.yaml
This project uses a configuration file (config.yaml) to store important directory paths and file lists, making it easier to manage input and output data files without hardcoding them.

data_dir: Dice_Game_Datasets

files:
- user
- user_registration
- user_play_session
- user_plan
- user_payment_detail
- plan
- plan_payment_frequency
- channel_code
- status_code

output_dir: output/csvs

Explanation
data_dir: The folder where your raw input CSV files are stored. For example, Dice_Game_Datasets/user.csv, Dice_Game_Datasets/plan.csv, etc.

files: A list of all the datasets (without the .csv extension) that the ETL process will load. Each entry here represents a CSV file (e.g. user.csv, user_plan.csv).

output_dir: The directory where all transformed and cleaned output CSV files will be saved.

## Project Folder Structure
/assessment
│── config.yaml # configuration file which contains config details i.e.data files,
                  output folder etc.
├── main.py # Main script to run the ETL pipeline and generate insights
│
├── etl/ # ETL package containing extraction, transformation logic
│ ├── loader.py # Data loading functions to read CSV files
│ ├── transformer.py # Data transformation logic to prepare fact and dimension tables
│ └── insights.py # Functions to generate insights from transformed data
│
├── tests/ # Unit tests for ETL modules and insights generation
│ ├── test_loader.py # Tests for loader functions
│ ├── test_transformer.py # Tests for transformer functions
│ └── test_insights.py # Tests for insights generation functions
│
├── data/ # Folder where input CSV files should be placed (configured in loader.py)
│ ├── user.csv
│ ├── user_registration.csv
│ ├── user_play_session.csv
│ ├── user_plan.csv
│ ├── user_payment_detail.csv
│ ├── plan.csv
│ ├── plan_payment_frequency.csv
│ ├── channel_code.csv
│ └── status_code.csv
│
└── output/ # Output folder where transformed CSV files for facts and dimensions are saved
└── csvs/
├── dim_user.csv
├── dim_user_registration.csv
├── dim_plan.csv
├── dim_payment_frequency.csv
├── dim_channel.csv
├── dim_status_code.csv
├── fact_play_sessions.csv
└── fact_user_payments.csv


## Requirements and Steps to excute the program

- Python 3.9+
- pandas
- pytest

Install dependencies with:

```bash
pip install -r requirements.txt

3. Run the program
Run the main script:

python main.py
This script will:

Load all source data from CSV files

Transform the data into dimensions and fact tables

Generate and print insights to the console

Save transformed data to output CSV files.


4. Run tests
To verify everything is working correctly, run:

pytest tests/

Troubleshooting
Make sure the CSV files exist and contain the expected columns.

Confirm that DATA_DIR in etl/loader.py points to the directory containing your CSVs.

If any tests fail, check the test error messages for missing keys or columns.

```

This will get your Dice Game ETL & Insights pipeline running smoothly!