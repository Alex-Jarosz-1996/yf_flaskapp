from datetime import datetime
from typing import Dict, Optional, Union


def getPrice(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        price = obj["currentPrice"]
    except Exception as e:
        print('Error in getPrice() function')
        print(e)
        return None
    else:
        return float(price)


def getMarketCap(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        mc = obj["marketCap"]
    except Exception as e:
        print('Error in getMarketCap() function')
        print(e)
        return None
    else:
        return float(mc)
    

def getNumSharesAvail(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        numShares = obj["sharesOutstanding"]
    except Exception as e:
        print('Error in getNumSharesAvail() function')
        print(e)
        return None
    else:
        return float(numShares)
    

def getYearlyLowPrice(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        ylp = obj["fiftyTwoWeekLow"]
    except Exception as e:
        print('Error in getYearlyLowPrice() function')
        print(e)
        return None
    else:
        return float(ylp)
    

def getYearlyHighPrice(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        yhp = obj["fiftyTwoWeekHigh"]
    except Exception as e:
        print('Error in getYearlyHighPrice() function')
        print(e)
        return None
    else:
        return float(yhp)
    

def getFiftyDayAverage(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        fiftyDayAvg = obj["fiftyDayAverage"]
    except Exception as e:
        print('Error in getFiftyDayAverage() function')
        print(e)
        return None
    else:
        return float(fiftyDayAvg)
    

def getTwoHundredDayAverage(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        twoHundredDayAvg = obj["twoHundredDayAverage"]
    except Exception as e:
        print('Error in getTwoHundredDayAverage() function')
        print(e)
        return None
    else:
        return float(twoHundredDayAvg)
    

def getAcquirersMultiple(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        mc = obj["marketCap"]
        td = obj["totalDebt"]
        tc = obj["totalCash"]
        ni = obj["netIncomeToCommon"]
        
        am = (mc + td - tc) / ni
    except Exception as e:
        print('Error in getAcquirersMultiple() function')
        print(e)
        return None
    else:
        return round(float(am), num_dp)


def getCurrentRatio(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        cr = obj["currentRatio"]
    except Exception as e:
        print('Error in getCurrentRatio() function')
        print(e)
        return None
    else:
        return round(float(cr), num_dp)
        

def getEnterpriseValue(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        mc = obj["marketCap"]
        td = obj["totalDebt"]
        tc = obj["totalCash"]
        
        ev = (mc + td - tc)
    except Exception as e:
        print('Error in getEnterpriseValue() function')
        print(e)
        return None
    else:
        return round(float(ev), num_dp)
        

def getEPS(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        eps = obj["trailingEps"]
    except Exception as e:
        print('Error in getEPS() function')
        print(e)
        return None
    else:
        return round(float(eps), num_dp)
    

def getEV_ToEBITDA(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        mc  = obj["marketCap"]
        td  = obj["totalDebt"]
        tc  = obj["totalCash"]
        ebitda = obj["ebitda"]
        
        ev2ebitda = (mc + td - tc) / ebitda
    except Exception as e:
        print('Error in getEV_ToEBITDA() function')
        print(e)
        return None
    else:
        return round(float(ev2ebitda), num_dp)
    

def getEV_ToRevenue(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        mc  = obj["marketCap"]
        td  = obj["totalDebt"]
        tc  = obj["totalCash"]
        rev = obj["totalRevenue"]

        ev2rev = (mc + td - tc) / rev
    except Exception as e:
        print('Error in getEV_ToRevenue() function')
        print(e)
        return None
    else:
        return round(float(ev2rev), num_dp)
    

def getPE_RatioTrail(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        peTrail = obj["trailingPE"]
    except Exception as e:
        print('Error in getPE_RatioTrail() function')
        print(e)
        return None
    else:
        return round(float(peTrail), num_dp)
    

def getPE_RatioForward(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        peForward = obj["forwardPE"]
    except Exception as e:
        print('Error in getPE_RatioForward() function')
        print(e)
        return None
    else:
        return round(float(peForward), num_dp)
    

def getPriceToSales(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        price2Sales = obj["priceToSalesTrailing12Months"]
    except Exception as e:
        print('Error in getPriceToSales() function')
        print(e)
        return None
    else:
        return round(float(price2Sales), num_dp)
    

def getPriceToBook(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        price2Book = obj["priceToBook"]
    except Exception as e:
        print('Error in getPriceToBook() function')
        print(e)
        return None
    else:
        return round(float(price2Book), num_dp)
    

def getDividendYield(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        divYield = obj["trailingAnnualDividendYield"]
    except Exception as e:
        print('Error in getDividendYield() function')
        print(e)
        return None
    else:
        return float(divYield)
    

def getDividendRate(obj: Dict[str, Optional[Union[int, float, str]]]) -> float:
    try:
        divRate = obj["dividendRate"]
    except Exception as e:
        print('Error in getDividendRate() function')
        print(e)
        return None
    else:
        return float(divRate)
    

def getExDivdate(obj: Dict[str, Optional[Union[int, float, str]]]) -> str:
    try:
        exDivDate = obj["exDividendDate"]
    except Exception as e:
        print('Error in getExDivdate() function')
        print(e)
        return None
    else:
        exDivDate_tstamp = datetime.fromtimestamp(exDivDate)
        exDivDate_formatted = f"{exDivDate_tstamp.day:02d}/{exDivDate_tstamp.month:02d}/{exDivDate_tstamp.year}"
        return str(exDivDate_formatted)
    

def getPayoutRatio(obj: Dict[str, Optional[Union[int, float, str]]]) -> str:
    try:
        payoutRatio = obj["payoutRatio"]
    except Exception as e:
        print('Error in getPayoutRatio() function')
        print(e)
        return None
    else:
        return str(payoutRatio)
    

def getBookValuePerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        bv = obj["bookValue"]
        ns = obj["sharesOutstanding"]
        
        bv2shares = bv / ns
    except Exception as e:
        print('Error in getBookValuePerShare() function')
        print(e)
        return None
    else:
        return round(float(bv2shares), num_dp)
    

def getCash(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        cash = obj["totalCash"]
    except Exception as e:
        print('Error in getCash() function')
        print(e)
        return None
    else:
        return round(float(cash), num_dp)
    

def getCashPerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        cashPerShare = obj["totalCashPerShare"]
    except Exception as e:
        print('Error in getCashPeShare() function')
        print(e)
        return None
    else:
        return round(float(cashPerShare), num_dp)
    

def getCashToMarketCap(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        tc = obj["totalCash"]
        mc = obj["marketCap"]

        cash2mc = tc / mc
    except Exception as e:
        print('Error in getCashToMarketCap() function')
        print(e)
        return None
    else:
        return round(float(cash2mc), num_dp)
    

def getCashToDebt(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        tc = obj["totalCash"]
        td = obj["totalDebt"]

        cash2debt = tc / td
    except Exception as e:
        print('Error in getCashToDebt() function')
        print(e)
        return None
    else:
        return round(float(cash2debt), num_dp)
    

def getDebt(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        td = obj["totalDebt"]
    except Exception as e:
        print('Error in getDebt() function')
        print(e)
        return None
    else:
        return round(float(td), num_dp)
    

def getDebtToMarketCap(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        td = obj["totalDebt"]
        mc = obj["marketCap"]

        debt2marketCap = td / mc
    except Exception as e:
        print('Error in getDebtToMarketCap() function')
        print(e)
        return None
    else:
        return round(float(debt2marketCap), num_dp)
    

def getDebtToEquity(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        de = obj["debtToEquity"]
    except Exception as e:
        print('Error in getDebtToEquity() function')
        print(e)
        return None
    else:
        return round(float(de), num_dp)
    

def getReturnToAssets(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        roa = obj["returnOnAssets"]
    except Exception as e:
        print('Error in getReturnToAssets() function')
        print(e)
        return None
    else:
        return round(float(roa), num_dp)
    

def getReturnToEquity(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        roe = obj["returnOnEquity"]
    except Exception as e:
        print('Error in getReturnToEquity() function')
        print(e)
        return None
    else:
        return round(float(roe), num_dp)
    

def getEBITDA(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ebitda = obj["ebitda"]
    except Exception as e:
        print('Error in getEBITDA() function')
        print(e)
        return None
    else:
        return round(float(ebitda), num_dp)


def getEBITDA_PerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ebitda = obj["ebitda"]
        numShares = obj["sharesOutstanding"]

        ebitdaPerShare = ebitda / numShares
    except Exception as e:
        print('Error in getEBITDA_PerShare() function')
        print(e)
        return None
    else:
        return round(float(ebitdaPerShare), num_dp)
    

def getEarningsGrowth(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        eg = obj["earningsGrowth"]
    except Exception as e:
        print('Error in getEarningsGrowth() function')
        print(e)
        return None
    else:
        return round(float(eg), num_dp)
    

def getGrossProfit(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        profits = obj["grossProfits"]
    except Exception as e:
        print('Error in getGrossProfit() function')
        print(e)
        return None
    else:
        return round(float(profits), num_dp)
    

def getGrossProfitPerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        profits = obj["grossProfits"]
        ns      = obj["sharesOutstanding"]

        profitsPerShare = profits / ns
    except Exception as e:
        print('Error in getGrossProfitPerShare() function')
        print(e)
        return None
    else:
        return round(float(profitsPerShare), num_dp)
    

def getNetIncome(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ni = obj["netIncomeToCommon"]
    except Exception as e:
        print('Error in getNetIncome() function')
        print(e)
        return None
    else:
        return round(float(ni), num_dp)
    

def getNetIncomePerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ni = obj["netIncomeToCommon"]
        ns = obj["sharesOutstanding"]

        niPerShare = ni / ns
    except Exception as e:
        print('Error in getNetIncomePerShare() function')
        print(e)
        return None
    else:
        return round(float(niPerShare), num_dp)
    

def getOperatingMargin(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        om = obj["operatingMargins"]
    except Exception as e:
        print('Error in getOperatingMargin() function')
        print(e)
        return None
    else:
        return round(float(om), num_dp)
    

def getProfitMargin(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        pm = obj["profitMargins"]
    except Exception as e:
        print('Error in getProfitMargin() function')
        print(e)
        return None
    else:
        return round(float(pm), num_dp)
    

def getRevenue(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        rev = obj["totalRevenue"]
    except Exception as e:
        print('Error in getRevenue() function')
        print(e)
        return None
    else:
        return round(float(rev), num_dp)
    

def getRevenueGrowth(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        revGrowth = obj["revenueGrowth"]
    except Exception as e:
        print('Error in getRevenueGrowth() function')
        print(e)
        return None
    else:
        return round(float(revGrowth), num_dp)
    

def getRevenueGrowthPerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        rgs = obj["revenuePerShare"]
    except Exception as e:
        print('Error in getRevenueGrowthPerShare() function')
        print(e)
        return None
    else:
        return round(float(rgs), num_dp)
    

def getFCF(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        fcf = obj["freeCashflow"]
    except Exception as e:
        print('Error in getFCF() function')
        print(e)
        return None
    else:
        return round(float(fcf), num_dp)
    

def getFCF_ToMarketCap(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        fcf = obj["freeCashflow"]
        mc  = obj["marketCap"]

        fcf2mc = fcf / mc
    except Exception as e:
        print('Error in getFCF_ToMarketCap() function')
        print(e)
        return None
    else:
        return round(float(fcf2mc), num_dp)
    

def getFCF_PerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        fcf = obj["freeCashflow"]
        ns  = obj["sharesOutstanding"]

        fcf2ns = fcf / ns
    except Exception as e:
        print('Error in getFCF_PerShare() function')
        print(e)
        return None
    else:
        return round(float(fcf2ns), num_dp)
    

def getFCF_ToEV(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        fcf = obj["freeCashflow"]
        mc = obj["marketCap"]
        td = obj["totalDebt"]
        tc = obj["totalCash"]

        fcf2EV = (fcf / (mc + td - tc))
    except Exception as e:
        print('Error in getFCF_ToEV() function')
        print(e)
        return None
    else:
        return round(float(fcf2EV), num_dp)
    

def getOCF(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ocf = obj["operatingCashflow"]
    except Exception as e:
        print('Error in getOCF() function')
        print(e)
        return None
    else:
        return round(float(ocf), num_dp)


def getOCF_ToRevenue(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ocf = obj["operatingCashflow"]
        rev = obj["totalRevenue"]

        ocf2rev = ocf / rev
    except Exception as e:
        print('Error in getOCF_ToRevenue() function')
        print(e)
        return None
    else:
        return round(float(ocf2rev), num_dp)


def getOCF_ToMarketCap(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ocf = obj["operatingCashflow"]
        mc  = obj["marketCap"]

        ocf2mc = ocf / mc
    except Exception as e:
        print('Error in getOCF_ToMarketCap() function')
        print(e)
        return None
    else:
        return round(float(ocf2mc), num_dp)


def getOCF_PerShare(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ocf = obj["operatingCashflow"]
        ns  = obj["sharesOutstanding"]

        ocf2ns = ocf / ns
    except Exception as e:
        print('Error in getOCF_PerShare() function')
        print(e)
        return None
    else:
        return round(float(ocf2ns), num_dp)


def getOCF_ToEV(obj: Dict[str, Optional[Union[int, float, str]]], num_dp: int) -> float:
    try:
        ocf = obj["operatingCashflow"]
        mc = obj["marketCap"]
        td = obj["totalDebt"]
        tc = obj["totalCash"]

        ocf2EV = (ocf / (mc + td - tc))
    except Exception as e:
        print('Error in getOCF_ToEV() function')
        print(e)
        return None
    else:
        return round(float(ocf2EV), num_dp)
