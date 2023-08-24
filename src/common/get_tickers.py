import os
import pandas as pd

def get_all_asx_tickers():
    current_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_dir, '../../company_lists/asx_companies.csv')
    df = pd.read_csv(csv_file_path)
    return df["ASX code"]

def get_all_us_tickers():
    current_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_dir, '../../company_lists/us_companies.csv')
    df = pd.read_csv(csv_file_path)
    return df["Symbol"]
