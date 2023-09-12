import os

from src.common.get_tickers import cleansed_asx_stocklist, cleansed_us_stocklist
from src.aus.aus_stock_class import AusStockClass
from src.us.us_stock_class import US_StockClass

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring db
db_path = os.path.join(os.path.dirname(__file__), 'stock_scrapper_app.db')
db_uri = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

# Define the database model
class StockCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=False, nullable=False)
    market = db.Column(db.String(10), nullable=False)

    def __init__(self, code, market):
        self.code = code
        self.market = market

def populate_db():
    asx_codes = cleansed_asx_stocklist()
    for code in asx_codes:
        stock = StockCode(code=code, market='AUS')
        db.session.add(stock)

    us_codes = cleansed_us_stocklist()
    for code in us_codes:
        stock = StockCode(code=code, market='US')
        db.session.add(stock)

    db.session.commit()

@app.route('/')
def core():
    return render_template("index.html")


@app.route('/get_stocks/<country>')
def get_stocks(country):
    if country == 'Australia':
        stock_codes = [stock.code for stock in StockCode.query.filter_by(market='AUS')]
    elif country == 'US':
        stock_codes = [stock.code for stock in StockCode.query.filter_by(market='US')]
    else:
        stock_codes = []

    return jsonify(stock_codes)


@app.route('/get_stock_info/<country>/<stock_code>')
def get_stock_info(country, stock_code):
    # Create an instance of AusStockClass with the selected stock code
    if country == 'Australia':
        stock_instance = AusStockClass(stock_code)
    else:
        stock_instance = US_StockClass(stock_code)

    # Return a JSON representation of the stock attributes
    return jsonify({
        'price': stock_instance.price,
        'marketCap': stock_instance.marketCap,
        'numSharesAvail': stock_instance.numSharesAvail,
        'yearlyLowPrice': stock_instance.yearlyLowPrice,
        'yearlyHighPrice': stock_instance.yearlyHighPrice,
        'fiftyDayMA': stock_instance.fiftyDayMA,
        'twoHundredDayMA': stock_instance.twoHundredDayMA,
        'acquirersMultiple': stock_instance.acquirersMultiple,
        'currentRatio': stock_instance.currentRatio,
        'enterpriseValue': stock_instance.enterpriseValue,
        'eps': stock_instance.eps,
        'evToEBITDA': stock_instance.evToEBITDA,
        'evToOperatingCashFlow': stock_instance.evToOperatingCashFlow,
        'evToRev': stock_instance.evToRev,
        'peRatioTrail': stock_instance.peRatioTrail,
        'peRatioForward': stock_instance.peRatioForward,
        'priceToSales': stock_instance.priceToSales,
        'priceToBook': stock_instance.priceToBook,
        'dividendYield': stock_instance.dividendYield,
        'dividendRate': stock_instance.dividendRate,
        'exDivDate': stock_instance.exDivDate,
        'payoutRatio': stock_instance.payoutRatio,
        'bookValPerShare': stock_instance.bookValPerShare,
        'cash': stock_instance.cash,
        'cashPerShare': stock_instance.cashPerShare,
        'cashToMarketCap': stock_instance.cashToMarketCap,
        'cashToDebt': stock_instance.cashToDebt,
        'debt': stock_instance.debt,
        'debtToMarketCap': stock_instance.debtToMarketCap,
        'debtToEquityRatio': stock_instance.debtToEquityRatio,
        'returnOnAssets': stock_instance.returnOnAssets,
        'returnOnEquity': stock_instance.returnOnEquity,
        'ebitda': stock_instance.ebitda,
        'ebitdaPerShare': stock_instance.ebitdaPerShare,
        'earningsGrowth': stock_instance.earningsGrowth,
        'grossProfit': stock_instance.grossProfit,
        'grossProfitPerShare': stock_instance.grossProfitPerShare,
        'netIncome': stock_instance.netIncome,
        'netIncomePerShare': stock_instance.netIncomePerShare,
        'operatingMargin': stock_instance.operatingMargin,
        'profitMargin': stock_instance.profitMargin,
        'revenue': stock_instance.revenue,
        'revenueGrowth': stock_instance.revenueGrowth,
        'revenuePerShare': stock_instance.revenuePerShare,
        'fcf': stock_instance.fcf,
        'fcfToMarketCap': stock_instance.fcfToMarketCap,
        'fcfPerShare': stock_instance.fcfPerShare,
        'ocf': stock_instance.ocf,
        'ocfToRevenueRatio': stock_instance.ocfToRevenueRatio,
        'ocfToMarketCap': stock_instance.ocfToMarketCap,
        'ocfPerShare': stock_instance.ocfPerShare,
        'fcfToEV': stock_instance.fcfToEV,
        'ocfToEV': stock_instance.ocfToEV
    })


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        populate_db()
    app.run(debug=True)
