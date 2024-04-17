## **Exchange Methods**
The exchange methods will help you get information about a specific exchange such as the Nigerian Stock Exchange or the Botswana Stock Exchange.

Afrimarket currently defines 4 methods to help you interact with information about an exchange. To use any of these methods, you have to first define an exchange to work with. Here's a simple example using the Nigerian Stock Exchange:
```python
import afrimarket as afm

# get all the available exchanges
markets= afm.markets

# specify an exchange
ngx = afm.Exchange(market='ngx')
```
!!! note
    You can visit the [markets page](./markets.md) to learn more about the exchanges in Afrimarket.


### **get_index_price**
The `get_index_price` method returns the index price for a specified exchange starting from April 2014 to the present day. Here's how to use this method:

```python
ngx = afm.Exchange(market='ngx')

# get the index price for the Nigerian Stock Exchange
index_price = ngx.get_index_price()

print(index_price)
```
The code above should return a data frame that you can use within your code. The data frame will contain the date and corresponding index price of the exchange. Here's the output of the code above:

```shell
           Date      Price
0    2014-04-16   39298.97
1    2014-04-17   39325.98
2    2014-04-22   39408.33
3    2014-04-23   39194.09
4    2014-04-24   39011.90
...         ...        ...
2436 2024-04-03  104181.32
2437 2024-04-04  103736.08
2438 2024-04-05  103437.67
2439 2024-04-08  103047.23
2440 2024-04-12  102314.56

[2441 rows x 2 columns]
```

### **get_listed_companies**
The `get_listed_companies` method returns a data frame with information about all the companies available in that exchange. The data frame contains 5 columns namely `Ticker`, `Name`, `Volume`, `Price`, and `Change`.

Here's a simple example demonstrating how to use the `get_listed_companies` method for the Nigerian stock exchange:
```Python
ngx=afm.Exchange(market='ngx')

listed_companies= ngx.get_listed_companies()

print(listed_companies)
```

The code above will return a data frame like this:

```shell
         Ticker                        Name      Volume  Price  Change
0      ABBEYBDS     Abbey Mortgage Bank Plc      6525.0   2.50    0.00
1      ABCTRANS      Associated Bus Company     87977.0   0.70    0.00
2       ACADEMY               Academy Press    111305.0   1.74    0.00
3    ACCESSCORP         Access Holdings Plc  12505059.0  18.85   -0.45
4     AFRINSURE  African Alliance Insurance         NaN   0.20     NaN
..          ...                         ...         ...    ...     ...
149    VITAFOAM            Vitafoam Nigeria    297219.0  21.00    0.00
150       WAPCO               Lafarge Wapco    381880.0  33.50    0.00
151       WAPIC             Wapic Insurance    253147.0   0.67   -0.01
152    WEMABANK                   Wema Bank   2718691.0   7.20   -0.70
153  ZENITHBANK             Zenith Bank Plc   7991666.0  39.00   -1.00

[154 rows x 5 columns]
```

<!-- ### **get_top_gainers**
The `get_top_gainers` method will return a data frame containing  -->


<!-- ### **get_bottom_losers** -->


## **Stock Methods**
Stock methods help you interact with a specific stock available in your preferred Exchange. The following methods are available in Afrimarket.

### **get_price**

### **get_last_trading_results**
