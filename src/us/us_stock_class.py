import yfinance as yf
# from src.us.us_stock_methods import *
try:
    from src.us.us_stock_methods import *
except:
    from us_stock_methods import *

class US_StockClass:
    def __init__(self, ticker): 

        num_dp = 3
        
        # setting up the below metrics
        self.obj  = yf.Ticker(f'{ticker}')
        self.info = self.obj.info
        
        # stock price metrics
        self.ticker          = ticker
        self.price           = getPrice(self.info)
        self.marketCap       = getMarketCap(self.info)
        self.numSharesAvail  = getNumSharesAvail(self.info)
        self.yearlyLowPrice  = getYearlyLowPrice(self.info)
        self.yearlyHighPrice = getYearlyHighPrice(self.info)
        self.fiftyDayMA      = getFiftyDayAverage(self.info)
        self.twoHundredDayMA = getTwoHundredDayAverage(self.info)

        # value metrics
        self.acquirersMultiple = getAcquirersMultiple(self.info, num_dp)
        self.currentRatio      = getCurrentRatio(self.info, num_dp)
        self.enterpriseValue   = getEnterpriseValue(self.info, num_dp)
        self.eps               = getEPS(self.info, num_dp)
        self.evToEBITDA        = getEV_ToEBITDA(self.info, num_dp)
        self.evToRev           = getEV_ToRevenue(self.info, num_dp)
        self.peRatioTrail      = getPE_RatioTrail(self.info, num_dp)
        self.peRatioForward    = getPE_RatioForward(self.info, num_dp)
        self.priceToSales      = getPriceToSales(self.info, num_dp)
        self.priceToBook       = getPriceToBook(self.info, num_dp)

        # # dividend metrics
        self.dividendYield = getDividendYield(self.info)
        self.dividendRate  = getDividendRate(self.info)
        self.exDivDate     = getExDivdate(self.info)
        self.payoutRatio   = getPayoutRatio(self.info)

        # # balance sheet metrics
        self.bookValPerShare   = getBookValuePerShare(self.info, num_dp)
        self.cash              = getCash(self.info, num_dp)
        self.cashPerShare      = getCashPerShare(self.info, num_dp)
        self.cashToMarketCap   = getCashToMarketCap(self.info, num_dp)
        self.cashToDebt        = getCashToDebt(self.info, num_dp)
        self.debt              = getDebt(self.info, num_dp)
        self.debtToMarketCap   = getDebtToMarketCap(self.info, num_dp)
        self.debtToEquityRatio = getDebtToEquity(self.info, num_dp)
        self.returnOnAssets    = getReturnToAssets(self.info, num_dp)
        self.returnOnEquity    = getReturnToEquity(self.info, num_dp)

        # # income related
        self.ebitda              = getEBITDA(self.info, num_dp)
        self.ebitdaPerShare      = getEBITDA_PerShare(self.info, num_dp)
        self.earningsGrowth      = getEarningsGrowth(self.info, num_dp)
        self.grossProfit         = getGrossProfit(self.info, num_dp)
        self.grossProfitPerShare = getGrossProfitPerShare(self.info, num_dp)
        self.netIncome           = getNetIncome(self.info, num_dp)
        self.netIncomePerShare   = getNetIncomePerShare(self.info, num_dp)
        self.operatingMargin     = getOperatingMargin(self.info, num_dp)
        self.profitMargin        = getProfitMargin(self.info, num_dp)
        self.revenue             = getRevenue(self.info, num_dp)
        self.revenueGrowth       = getRevenueGrowth(self.info, num_dp)
        self.revenuePerShare     = getRevenueGrowthPerShare(self.info, num_dp)

        # # cash flow related
        self.fcf               = getFCF(self.info, num_dp)
        self.fcfToMarketCap    = getFCF_ToMarketCap(self.info, num_dp)
        self.fcfPerShare       = getFCF_PerShare(self.info, num_dp)
        self.fcfToEV           = getFCF_ToEV(self.info, num_dp)
        self.ocf               = getOCF(self.info, num_dp)
        self.ocfToRevenueRatio = getOCF_ToRevenue(self.info, num_dp)
        self.ocfToMarketCap    = getOCF_ToMarketCap(self.info, num_dp)
        self.ocfPerShare       = getOCF_PerShare(self.info, num_dp)
        self.ocfToEV           = getOCF_ToEV(self.info, num_dp)
        

    def get_stock_properties(self):
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


    def get_all_keys(self):
        """
        returns all possible keys that is available to the developer
        """
        for i in self.info.keys():
            print(i)


    def print_all_class_properties(self):
        """
        prints all properties
        """
        print(', '.join("%s: %s" % item for item in vars(US_StockClass(f'{self.ticker}')).items()))


    def get_all_properties(self):
        properties = {}

        for attr_name in dir(self):
            attr_value = getattr(self, attr_name)
            if not callable(attr_value) and not attr_name.startswith("__"):
                properties[attr_name] = attr_value

        return properties


if __name__ == "__main__":
    stock = US_StockClass("AAPL")
    all_properties = stock.get_all_properties()
    for prop_name, prop_value in all_properties.items():
        print(f"{prop_name}: {prop_value}")