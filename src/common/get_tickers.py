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

def cleanse_stocklist(stocks: pd.DataFrame):
    for stock in stocks:
        if not isinstance(stock, str):
            stock = str(stock)
        
        if " " in stock:
            stock = stock.replace(" ", "")
        elif "\n" in stock:
            stock = stock.replace("\n", "")
        else:
            pass  # potentially need to do regex checks here

    return stocks
