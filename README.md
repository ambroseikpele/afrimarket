## Quick Start


```python

import afrimarket as afm

uba = afm.Stock(ticker=“uba”, market= “ngx”)

price= uba.get_price()

print(price)
