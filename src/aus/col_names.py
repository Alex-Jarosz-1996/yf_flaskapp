from enum import Enum

class AusColNames(Enum):
    ticker = 1
    price = 2
    marketCap = 3
    numSharesAvail = 4
    yearLowPrice = 5
    yearHighPrice = 6
    MA_50Day = 7
    MA_200Day = 8
    acquirersMultiple = 9
    evRToRev = 10
    evToEBITDA = 11
    EnterpriseValue = 12
    PE_RatioTrail = 13
    PE_RatioForw = 14
    priceToSales = 15
    priceToBook = 16
    bookValuePerShare = 17
    cashPerShare = 18
    cashMarketCap = 19
    cashToDebt = 20
    currentRatio = 21
    debtToMarketCap = 22
    debtToEquity = 23
    earningsPerShare = 24
    EBITDA_PerShare = 25
    grossProfitPerShare = 26
    netIncomePerShare = 27
    netIncomeMarginRatio = 28
    revenuePerShare = 29
    enterpriseValueToOCF = 30
    OCF_ToRevenue = 31