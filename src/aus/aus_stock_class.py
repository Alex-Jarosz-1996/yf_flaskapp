from src.aus.aus_stock_methods import *
from src.aus.websites import *


class AusStockClass:
    """
    Class for Australian only stocks
    """
    def __init__(self, stock: str):
        # setting up the below metrics
        self.ticker = stock 
        mwData = marketWatchData(self.ticker)
        yfData = yahooFinanceData(self.ticker)

        # stock price metrics
        self.price           = getPrice(mwData)
        self.marketCap       = getMarketCap(yfData)
        self.numSharesAvail  = getNumberOfSharesOutstanding(yfData)
        self.yearlyLowPrice  = get52_WkLowPrice(yfData)
        self.yearlyHighPrice = get52_WkHighPrice(yfData)
        self.fiftyDayMA      = get50_DayMovingAverage(yfData)
        self.twoHundredDayMA = get200_DayMovingAverage(yfData)

        # value metrics
        self.acquirersMultiple = getAcquirersMultiple(yfData)
        self.currentRatio      = getCurrentRatio(yfData)
        self.enterpriseValue   = getEnterpriseValue(yfData)
        self.eps               = getEPS(yfData)
        self.evToEBITDA        = getEV_ToEBITDA(yfData)
        self.evToRev           = getEV_ToRevenue(yfData)
        self.peRatioTrail      = getPE_ratioTrailing(yfData)
        self.peRatioForward    = getPE_ratioForward(yfData)
        self.priceToSales      = getPriceToSales(yfData)
        self.priceToBook       = getPriceToBook(yfData)

        # dividend metrics
        self.dividendYield = getTrailingDividendYield(yfData)
        self.dividendRate  = getTrailingDividendRate(yfData)
        self.exDivDate     = getExDividendDate(yfData)
        self.payoutRatio   = getPayoutRatio(yfData)
        
        # balance sheet metrics
        self.bookValPerShare   = getBookValuePerShare(yfData)
        self.cash              = getCash(yfData)
        self.cashPerShare      = getCashPerShare(yfData)
        self.cashToMarketCap   = getCashToMarketCap(yfData)
        self.cashToDebt        = getCashToDebt(yfData)
        self.debt              = getDebt(yfData)
        self.debtToMarketCap   = getDebtToMarketCap(yfData)
        self.debtToEquityRatio = getDebtEquityRatio(yfData)
        self.returnOnAssets    = getReturnOnAssets(yfData)
        self.returnOnEquity    = getReturnOnEquity(yfData)
        
        # income related
        self.ebitda              = getEBITDA(yfData)
        self.ebitdaPerShare      = getEBITDA_perShare(yfData)
        self.earningsGrowth      = getEarningsGrowth(yfData)
        self.grossProfit         = getGrossProfit(yfData)
        self.grossProfitPerShare = getGrossProfitPerShare(yfData)
        self.netIncome           = getNetIncome(yfData)
        self.netIncomePerShare   = getNetIncomePerShare(yfData)
        self.operatingMargin     = getOperatingMargin(yfData)
        self.profitMargin        = getProfitMargin(yfData)
        self.revenue             = getRevenue(yfData)
        self.revenueGrowth       = getRevenueGrowth(yfData)
        self.revenuePerShare     = getRevenuePerShare(yfData)

        # cash flow related
        self.fcf               = getLeveredFreeCashFlow(yfData)
        self.fcfToMarketCap    = getLeveredFreeCashFlowToMarketCap(yfData)
        self.fcfPerShare       = getLeveredFreeCashFlowPerShare(yfData)
        self.fcfToEV           = getFreeCashFlowToEnterpriseValue(yfData)
        self.ocf               = getOperatingCashFlow(yfData)
        self.ocfToRevenueRatio = getOCF_toRevenueRatio(yfData)
        self.ocfToMarketCap    = getOperatingCashFlowToMarketCap(yfData)
        self.ocfPerShare       = getOperatingCashFlowPerShare(yfData)
        self.ocfToEV           = getOperatingCashFlowToEnterpriseValue(yfData)


    def get_stock_properties(self):
        """
        Returns all a dict type of all stock class properties
        """
        properties = {
            'price': self.price,
            'marketCap': self.marketCap,
            'numSharesAvail': self.numSharesAvail,
            'yearlyLowPrice': self.yearlyLowPrice,
            'yearlyHighPrice': self.yearlyHighPrice,
            'fiftyDayMA': self.fiftyDayMA,
            'twoHundredDayMA': self.twoHundredDayMA,

            'acquirersMultiple': self.acquirersMultiple,
            'currentRatio': self.currentRatio,
            'enterpriseValue': self.enterpriseValue,
            'eps': self.eps,
            'evToEBITDA': self.evToEBITDA,
            'evToRev': self.evToRev,
            'peRatioTrail': self.peRatioTrail,
            'peRatioForward': self.peRatioForward,
            'priceToSales': self.priceToSales,
            'priceToBook': self.priceToBook,

            'dividendYield': self.dividendYield,
            'dividendRate': self.dividendRate,
            'exDivDate': self.exDivDate,
            'payoutRatio': self.payoutRatio,

            'bookValPerShare': self.bookValPerShare,
            'cash': self.cash,
            'cashPerShare': self.cashPerShare,
            'cashToMarketCap': self.cashToMarketCap,
            'cashToDebt': self.cashToDebt,
            'debt': self.debt,
            'debtToMarketCap': self.debtToMarketCap,
            'debtToEquityRatio': self.debtToEquityRatio,
            'returnOnAssets': self.returnOnAssets,
            'returnOnEquity': self.returnOnEquity,

            'ebitda': self.ebitda,
            'ebitdaPerShare': self.ebitdaPerShare,
            'earningsGrowth': self.earningsGrowth,
            'grossProfit': self.grossProfit,
            'grossProfitPerShare': self.grossProfitPerShare,
            'netIncome': self.netIncome,
            'netIncomePerShare': self.netIncomePerShare,
            'operatingMargin': self.operatingMargin,
            'profitMargin': self.profitMargin,
            'revenue': self.revenue,
            'revenueGrowth': self.revenueGrowth,
            'revenuePerShare': self.revenuePerShare,

            'fcf': self.fcf,
            'fcfToMarketCap': self.fcfToMarketCap,
            'fcfPerShare': self.fcfPerShare,
            'fcfToEV': self.fcfToEV,
            'ocf': self.ocf,
            'ocfToRevenueRatio': self.ocfToRevenueRatio,
            'ocfToMarketCap': self.ocfToMarketCap,
            'ocfPerShare': self.ocfPerShare,
            'ocfToEV': self.ocfToEV
        }
        return properties


    def __repr__(self):
        return self


    def __str__(self):
        return self

    
    def get_all_properties(self):
        """
        Returns all properties.
        """
        properties = {}

        for attr_name in dir(self):
            attr_value = getattr(self, attr_name)
            if not callable(attr_value) and not attr_name.startswith("__"):
                properties[attr_name] = attr_value

        return properties
