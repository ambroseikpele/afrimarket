## Quick Start

```python

# Get exchange stock market information
markets= afm.markets

ngx=afm.Exchange(market=markets['Nigerian Stock Exchange'])

listed_companies= ngx.get_listed_companies()

bottom_losers= ngx.get_bottom_losers()

print(listed_companies)

print(bottom_losers)


# Get the stock information of a company in a market

tlw = afm.Stock(ticker='TLW', market= markets['Ghana Stock Exchange'])

price= tlw.get_price()

growth_valuation= tlw.get_growth_and_valuation()

print(price)

print(growth_valuation)