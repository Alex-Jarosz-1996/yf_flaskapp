import os

from src.common.get_tickers import cleansed_asx_stocklist, cleansed_us_stocklist

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
def hello_world():
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


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        populate_db()
    app.run(debug=True)
