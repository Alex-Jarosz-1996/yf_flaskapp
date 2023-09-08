from yf_flaskapp.src.aus.aus_stock_methods import *
from websites import *

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
        self.evToRev               = getEV_ToRevenue(yfData)
        self.evToEBITDA            = getEV_ToEBITDA(yfData)
        self.enterpriseValue       = getEnterpriseValue(yfData)
        self.peRatioTrail          = getPE_ratioTrailing(yfData)
        self.peRatioForward        = getPE_ratioForward(yfData)
        self.priceToSales          = getPriceToSales(yfData)
        self.priceToBook           = getPriceToBook(yfData)
        self.bookValPerShare       = getBookValuePerShare(yfData)
        self.cashPerShare          = getCashPerShare(yfData)
        self.cashToMarketCap       = getCashToMarketCap(yfData)
        self.cashToDebt            = getCashToDebt(yfData)
        self.currentRatio          = getCurrentRatio(yfData)
        self.debtToMarketCap       = getDebtToMarketCap(yfData)
        self.debtToEquityRatio     = getDebtEquityRatio(yfData)
        self.eps                   = getEPS(yfData)
        self.ebitdaPerShare        = getEBITDA_perShare(yfData)
        self.grossProfitPerShare   = getGrossProfitPerShare(yfData)
        self.netIncomePerShare     = getNetIncomePerShare(yfData)
        self.netIncomeMarginRatio  = getNetIncomeMarginRatio(yfData)
        self.revenuePerShare       = getRevenuePerShare(yfData)
        self.evToOperatingCashFlow = getEnterpriseValueToOperatingCashFlow(yfData)
        self.ocfToRevenueRatio     = getOCF_toRevenueRatio(yfData)
        self.lfcfToMarketCap       = getLeveredFreeCashFlowToMarketCap(yfData)
        self.lfcfPerShare          = getLeveredFreeCashFlowPerShare(yfData)
        self.ocfToMarketCap        = getOperatingCashFlowToMarketCap(yfData)
        self.ocfPerShare           = getOperatingCashFlowPerShare(yfData)

        # dividend metrics
        self.exDivDate     = getExDividendDate(yfData)
        self.payoutRatio   = getPayoutRatio(yfData)
        self.forwDivYield  = getForwardDividendYield(yfData)
        self.forwDivRate   = getForwardDividendRate(yfData)
        self.trailDivYield = getTrailingDividendYield(yfData)
        self.trailDivRate  = getTrailingDividendRate(yfData)

        # balance sheet metrics
        self.cash           = getCash(yfData)
        self.debt           = getDebt(yfData)
        self.returnOnAssets = getReturnOnAssets(yfData)
        self.returnOnEquity = getReturnOnEquity(yfData)
        
        # income related
        self.earningsGrowth  = getEarningsGrowth(yfData)
        self.ebitda          = getEBITDA(yfData)
        self.grossProfit     = getGrossProfit(yfData)
        self.netIncome       = getNetIncome(yfData)
        self.operatingMargin = getOperatingMargin(yfData)
        self.profitMargin    = getProfitMargin(yfData)
        self.revenue         = getRevenue(yfData)
        self.revenueGrowth   = getRevenueGrowth(yfData)

        # cash flow related
        self.lfcf = getLeveredFreeCashFlow(yfData)
        self.ocf  = getOperatingCashFlow(yfData)

    def __repr__(self, obj):
        return obj

    def __str__(self, obj):
        return obj
