#python -m flask run --reload
import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta
from flask import Flask, request, render_template, send_file, send_from_directory
from forms import StockDataForm

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'quiniela2024'

@app.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), path)

def get_stock_data(tickers, start_date, end_date, interval):
    stock_data = yf.download(tickers, start=start_date, end=end_date,group_by='ticker', interval=interval)
    return stock_data

def write_to_excel(stock_data):
    writer = pd.ExcelWriter('stock_data.xlsx')
    stock_data.to_excel(writer)
    writer.save()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = StockDataForm()

    if form.validate_on_submit():
        tickers = form.tickers.data.replace(" ", "").upper().split(',')
        start_date = form.start_date.data.strftime('%Y-%m-%d')
        end_date = (form.end_date.data + timedelta(days=1)).strftime('%Y-%m-%d')
        interval = form.interval.data

        # Call the function that handles the data retrieval
        stock_data = get_stock_data(tickers, start_date, end_date, interval)
        write_to_excel(stock_data)
        print('sending form')
        return send_from_directory(directory=os.getcwd(), path='stock_data.xlsx', as_attachment=True)

    else:
        print('form not sent')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
