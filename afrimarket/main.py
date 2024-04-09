import requests
import pandas as pd
from datetime import datetime
from io import StringIO
import re


markets={
    'Botswana Stock Exchange':'bse',
    'Bourse Régionale des Valeurs Mobilières':'brvm',
    'Ghana Stock Exchange':'gse',
    'Johannesburg Stock Exchange':'jse',
    'Lusaka Securities Exchange':'luse',
    'Malawi Stock Exchange':'mse',
    'Nairobi Securities Exchange':'nse',
    'Nigerian Stock Exchange':'ngx',
    'Uganda Securities Exchange':'use',
    'Zimbabwe Stock Exchange':'zse'
}

class Exchange:
    def __init__(self, market) -> None:
        self.market=market
        self.market_url= f'https://afx.kwayisi.org/{self.market}/'
        self.market_price_url= f'https://afx.kwayisi.org/chart/{self.market}/'

    def get_index_price(self):
        content= str(requests.get(self.market_price_url).content)
        pattern = r'd\("(\d{4}-\d{2}-\d{2})"\),(\d+\.\d+)'
        matches = re.findall(pattern, content)
        date_price_list = []
        for match in matches:
            date_price_list.append((datetime.strptime(match[0], "%Y-%m-%d"), float(match[1])))
        df= pd.DataFrame(date_price_list, columns=['Date', 'Price'])
        return df
    
    def get_listed_companies(self):
        try:
            content = StringIO(str(requests.get(self.market_url).content))
            data = pd.read_html(content, match='Ticker')[0]

            i = 2
            previous_list = data['Ticker'].tolist()
            while True:
                new_url = f'{self.market_url}?page={i}'

                content = StringIO(str(requests.get(new_url).content))
                new_df = pd.read_html(content, match='Ticker')[0]
                
                new_list = new_df['Ticker'].tolist()
                
                if new_list == previous_list:
                    break
                else:
                    data = pd.concat([data, new_df], axis=0).reset_index(drop=True)
                    i += 1
                    previous_list = new_list

            return data
        except:
            print('Table Not Found')

    def get_top_gainers(self):
        try:
            content= StringIO(str(requests.get(self.market_url).content))
            data= pd.read_html(content, match='Top Gainers')[0]
            return data
        except:
            print('Table Not Found')

    def get_bottom_losers(self):
        try:
            content= StringIO(str(requests.get(self.market_url).content))
            data= pd.read_html(content, match='Bottom Losers')[0]
            return data
        except:
            print('Table Not Found')


    
class Stock(Exchange):
    def __init__(self, ticker, market) -> None:
        self.ticker=ticker.lower()
        super().__init__(market)

        self.price_url= f'https://afx.kwayisi.org/chart/{self.market}/{self.ticker}'
        self.url= f'https://afx.kwayisi.org/{self.market}/{self.ticker}.html'


    def get_price(self):
        content= str(requests.get(self.price_url).content)
        pattern = r'd\("(\d{4}-\d{2}-\d{2})"\),(\d+\.\d+)'
        matches = re.findall(pattern, content)
        date_price_list = []
        for match in matches:
            date_price_list.append((datetime.strptime(match[0], "%Y-%m-%d"), float(match[1])))
        df= pd.DataFrame(date_price_list, columns=['Date', 'Price'])
        return df
    
    def get_last_trading_results(self):
        try:
            content= StringIO(str(requests.get(self.url).content))
            data= pd.read_html(content, match='Last Trading Results')[0]
            return data
        except:
            print('Table Not Found')

    def get_growth_and_valuation(self):
        try:
            content= StringIO(str(requests.get(self.url).content))
            data= pd.read_html(content, match='Growth & Valuation')[0]
            return data
        except:
            print('Table Not Found')

    def get_stock_market_performance_period(self):
        try:
            content= StringIO(str(requests.get(self.url).content))
            data_first= pd.read_html(content, match='4WK')[0]
            data_second= pd.read_html(content, match='YTD')[0]
            return pd.concat([data_first, data_second], axis=1)
        except:
            print('Table Not Found')
    
    def get_stock_market_performance_date(self):
        try:
            content= StringIO(str(requests.get(self.url).content))
            data= pd.read_html(content, match='Change%')[0]
            return data
        except:
            print('Table Not Found')
    
    def get_competitors(self):
        try:
            content= StringIO(str(requests.get(self.url).content))
            data= pd.read_html(content, match='Code')[0]
            return data 
        except ValueError:
            print('Table Not Found')  
