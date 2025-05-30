import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', 'input.csv')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed', 'output.csv')

