Afrimarket is a Python package that provides stock information of any company in nine of the stock exchanges available in Africa. Afrimarket gives you access to information such as the price, trading results, and even competitors of the company you choose.

## Quick Start
Install the package using Pip:
```python
pip install afrimarket
```

This example shows you how to get the listed companies and bottom losers in the Nigerian Stock Exchange
```python
import afrimarket as afm

# Get exchange stock market information
markets= afm.markets

ngx=afm.Exchange(market=markets['Nigerian Stock Exchange'])

listed_companies= ngx.get_listed_companies()

bottom_losers= ngx.get_bottom_losers()

print(listed_companies)

print(bottom_losers)
```

Here's a code snippet for getting a company's price and growth valuation in a specific exchange using the ticker.
```python
import afrimarket as afm

# Get exchange stock market information
markets= afm.markets

# Get the stock information of a company in a market
tlw = afm.Stock(ticker='TLW', market= markets['Ghana Stock Exchange'])

price= tlw.get_price()

growth_valuation= tlw.get_growth_and_valuation()

print(price)

print(growth_valuation)
```

For more information, you should check out our [full documentation guide](https://afrimarket.readthedocs.io/en/latest/).
