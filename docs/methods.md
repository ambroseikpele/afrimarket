## Exchange Methods
The exchange methods will help you get information about a specific exchange such as the Nigerian Stock Exchange or the Botswana Stock exchange.

Afrimarket currently defines 4 methods to help you interact with information about an exchange. To use any of these methods, you have to firstly define an exchange to work with. Here's a simple example using the Nigerian Stock Exchange:
```python
import afrimarket as afm

markets= afm.markets # get all the available exchanges

ngx = afm.Exchange('ngx') # specify an exchange
```
!!! note
    You can visit the [markets page](./markets.md) to learn more about the exchanges in Afrimarket.


### get_index_price


### get_listed_companies


### get_top_gainers


### get_bottom_losers