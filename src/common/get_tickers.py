import os
import pandas as pd

from typing import List


def get_all_asx_tickers() -> pd.DataFrame:
    """
    Returns all ASX stock codes from asx_companies.csv
    """
    
    current_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_dir, '../../csv/asx_companies.csv')
    df = pd.read_csv(csv_file_path)
    return df["ASX code"]


def get_all_us_tickers() -> pd.DataFrame:
    """
    Returns all US stock codes from us_companies.csv
    """

    current_dir = os.path.dirname(__file__)
    csv_file_path = os.path.join(current_dir, '../../csv/us_companies.csv')
    df = pd.read_csv(csv_file_path)
    return df["Symbol"]


def cleanse_stocklist(stocks: pd.DataFrame) -> List[str]:
    """
    Removing duplicate stock codes, and unnecessary punctuation in stocklist
    """
    
    return_stockset = set()  # Using a set to track unique stock codes

    for stock in stocks:
        if not isinstance(stock, str):
            stock = str(stock)
        
        if " " in stock:
            stock = stock.replace(" ", "")
        elif "\n" in stock:
            stock = stock.replace("\n", "")
        else:
            pass  # potentially need to do regex checks here

        return_stockset.add(stock)  # Add stock to set (duplicates will be automatically ignored)

    return_stocklist = list(return_stockset)
    return return_stocklist


def cleansed_asx_stocklist() -> List[str]:
    """
    Cleansing ASX stock codes
    """
    
    codes = get_all_asx_tickers()
    return list(cleanse_stocklist(codes))


def cleansed_us_stocklist() -> List[str]:
    """
    Cleansing US stock codes
    """

    codes = get_all_us_tickers()
    return list(cleanse_stocklist(codes))
