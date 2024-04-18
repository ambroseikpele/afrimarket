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

### **get_top_gainers**
The `get_top_gainers` method will return a data frame with the highest gainers companies in that exchange. The data frame contains 3 columns: **Name**, **price**, and **percentage increase**. The **price** column represents the price per stock.
Here's how you can use this method:
```python
import afrimarket as afm

ngx=afm.Exchange(market='ngx')

print(ngx.get_top_gainers())
```

The code above will return a data frame like this:
```shell
              name                  price            %increase
0         GUINNESS               55.00            +10.00%
1          NEIMETH                1.80             +9.76%
2          MORISON                3.72             +9.73%
3       INTENEGINS                1.41             +9.30%
4         REGALINS                0.39             +8.33%
5         CORNERST                1.93             +3.76%
```


### **get_bottom_losers**
The ``get_bottom_losers` method simply returns the top companies who have accumulated the greatest amount of losses in the exchange. It returns a data frame with 3 columns; **name**, **price**, **%decrease**. The **price** column represents the price per stock. Here's an example:

```python
import afrimarket as afm

ngx=afm.Exchange(market='ngx')

print(ngx.get_bottom_losers())
```
The code above will return a data frame similar to this:
```shell
                Name                    Price             %decrease
0                CWG                  5.70              -11.63%
1               UCAP                 18.10               -9.73%
2         CONHALLPLC                  1.21               -9.70%
3              CHAMS                  1.69               -9.14%
4          SUNUASSUR                  1.00               -8.26%
5          GUINEAINS                  0.34               -8.11%
```

## **Stock Methods**
Stock methods help you interact with a specific stock available in your preferred Exchange. The following methods are available in Afrimarket.

### **get_price**
The `get_price` method returns the date and the price per stock of your chosen stock. Here is an example:
```python
import afrimarket as afm

uba = afm.Stock(ticker="uba", market= "ngx")

print(uba.get_price())
```
The above code will give the following output:

```shell
           Date  Price
0    2014-04-22   6.75
1    2014-04-23   6.85
2    2014-04-24   6.85
3    2014-04-25   6.91
4    2014-04-28   6.83
...         ...    ...
2263 2024-04-05  26.50
2264 2024-04-08  25.15
2265 2024-04-12  26.30
2266 2024-04-17  22.75
2267 2024-04-18  22.70

[2268 rows x 2 columns]
```
The **date** column returns a range of days dating back to 10 years from the present day. The **price** column returns the price per stock on the corresponding date.

### **get_last_trading_results**
This method returns the last trading result of the stock. Here's an example:
```python
import afrimarket as afm

uba = afm.Stock(ticker="uba", market= "ngx")

print(uba.get_last_trading_results())
```

The above code will return the following output:
```shell
0                Opening Price                    NaN
1                    Low Price                  22.65
2                    High Price                  23.20
3                Traded Volume                  28.4M
4              Number of Deals                    688
5               Gross Turnover                   650M
```
The data frame above shows the **Opening Price**, **Low Price**, **High Price** **Traded Volume**, **Number of Deals**, and **Gross Turnover** of the UBA stock in the Nigerian Stock Exchange.

### **get_stock_market_performance_period**
This method gives you information about how a stock performed over a given period of up to one year. Here is an example:

```python
import afrimarket as afm

uba = afm.Stock(ticker="uba", market= "ngx")

print(uba.get_stock_market_performance_period())
```
The code above will return an output like this:
```shell
      1WK     4WK     3MO     6MO    1YR     YTD
0  -9.74%  -8.84%  -33.1%  +26.5%  +166%  -11.5%
```
The **YTD** column represents the stock's performance from the beginning of the year to the current date.

### **get_stock_market_performance_date**
The **get_stock_market_performance_date** method returns a data frame containing information about a stock's performance over the last 10 days. Here's an example:
```python
import afrimarket as afm

uba = afm.Stock(ticker="uba", market= "ngx")

print(uba.get_stock_market_performance_date())
```
The code above will return an output like this:

```shell
         Date     Volume  Close  Change Change%
0  2024-04-18   28445087  22.70   -0.05  -0.22%
1  2024-04-17   55013392  22.75   -0.25  -1.09%
2  2024-04-16   45631809  23.00   -2.00  -8.00%
3  2024-04-15   42253586  25.00   -1.30  -4.94%
4  2024-04-12  148881854  26.30    1.15  +4.57%
5  2024-04-08    9025459  25.15   -1.35  -5.09%
6  2024-04-05   51378306  26.50     NaN     NaN
7  2024-04-04   47823335  26.50   -1.00  -3.64%
8  2024-04-03   49005699  27.50   -0.50  -1.79%
9  2024-04-02   65487378  28.00     NaN     NaN
```

### **get_competitors**
This method simply returns a data frame of stocks that are competing with your chosen stock. Here's an example that checks for the competitors of the UBA stock:
```python
import afrimarket as afm

uba = afm.Stock(ticker="uba", market= "ngx")

print(uba.get_competitors())
```

The code above will return an output like this:
```shell
         Code                           Name  M. Cap.  Close     YTD
0         ETI      Ecobank Transnational Inc    477B  26.00  +24.4%
1        FBNH               FBN Holdings Plc    967B  26.95  +14.4%
2  ZENITHBANK                Zenith Bank Plc   1.13T  36.00  -6.86%
3        GTCO         Guaranty Trust Holding   1.01T  34.35  -15.2%
4  FIDELITYBK              Fidelity Bank Plc    279B   8.70  -19.8%
5  ACCESSCORP            Access Holdings Plc    613B  17.25  -25.5%
6  VERITASKAP  Veritas Kapital Assurance Plc    8.6B   0.62  +67.6%
7         NEM       N.E.M. Insurance Company   52.2B  10.40  +65.1%
8    CORNERST  Cornerstone Insurance Company   35.1B   1.93  +37.9%
9  UNIVINSURE    Universal Insurance Company    5.6B   0.35  +34.6%
```
The output above contains the top 10 competitors of the UBA stock in the Nigerian Stock Exchange. The columns include **Code**, **Name**, **M.Cap.**, **Close**, and **YTD**. This table explains what they each mean:

|Column name | Meaning|
|------------|--------|
|Code|This represents the market ticker of the stock|
|Name|The company's full name|
|M. Cap.| The market capitalization of the stock|
|Close|The closing price of the stock|
|YTD|The percentage change in the stock's price from the beginning of the year till the current date|

