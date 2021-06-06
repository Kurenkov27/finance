import requests
import time
from datetime import datetime


def run_load_data(elems):
    for elem in elems:
        load_data(elem)


def load_data(elem):
    tt = datetime.now()
    period1 = 0
    period2 = int(time.mktime(time.strptime(tt.strftime('%Y-%m-%d %H:%M:%S'), "%Y-%m-%d %H:%M:%S")))
    period_url = f'?period1={period1}&period2={period2}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

    href_download = 'https://query1.finance.yahoo.com/v7/finance/download/' + elem + period_url
    response = requests.get(href_download, stream=True)

    with open(f'data/{elem}.csv', 'wb') as f:
        f.write(response.content)
