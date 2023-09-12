from src.aus.aus_stock_methods import *
from src.aus.websites import *

class AusStockClass:
    def __init__(self, stock: str):
        # 
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
        self.acquirersMultiple     = getAcquirersMultiple(yfData)
        self.currentRatio          = getCurrentRatio(yfData)
        self.enterpriseValue       = getEnterpriseValue(yfData)
        self.eps                   = getEPS(yfData)
        self.evToEBITDA            = getEV_ToEBITDA(yfData)
        self.evToOperatingCashFlow = getEnterpriseValueToOperatingCashFlow(yfData)
        self.evToRev               = getEV_ToRevenue(yfData)
        self.peRatioTrail          = getPE_ratioTrailing(yfData)
        self.peRatioForward        = getPE_ratioForward(yfData)
        self.priceToSales          = getPriceToSales(yfData)
        self.priceToBook           = getPriceToBook(yfData)

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
        self.ocf               = getOperatingCashFlow(yfData)
        self.ocfToRevenueRatio = getOCF_toRevenueRatio(yfData)
        self.ocfToMarketCap    = getOperatingCashFlowToMarketCap(yfData)
        self.ocfPerShare       = getOperatingCashFlowPerShare(yfData)
        self.fcfToEV           = self.fcf / self.enterpriseValue
        self.ocfToEV           = self.ocf / self.enterpriseValue


    def __repr__(self):
        return self


    def __str__(self):
        return self
