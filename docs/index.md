Afrimarket is a Python package that provides stock information of any company in nine of the stock exchanges available in Africa. Afrimarket gives you access to information such as thr price, trading results, and even competitiors of the company you choose.

## Installation
You can install Afrimarket with pip:

```shell
pip install afrimarket
```

## Usage
Afrimaket provides multiple methods to help you access information about the stock you want. Using Afrimaeket means you call these methods for your use case. Here's a simple example to get the current price of the Access Bank PLC in Botswana

```Python
import afrimarket as afm # import module

bse_access_stock = afm.Stock(ticker="ACCESS", market= "bse")  # initialize stock

price = bse_access_stock.get_price() # get stock price

print(price)
```
You can find a list of the methods and markets supported in Afrimarket on the [methods page](./methods.md) and [markets page](./markets.md) respectively.
