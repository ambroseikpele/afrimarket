import matplotlib.pyplot as plt
import numpy as np
import afrimarket as afm

uba_stock = afm.Stock("uba", market="ngx")
competitors = uba_stock.get_competitors()

tickers = ["UBA"]


# get the growth and valuation of the uba stock
uba_growth_val = uba_stock.get_growth_and_valuation()

# access the market capitalization row and retrieve its value
uba_market_cap = uba_growth_val.loc[uba_growth_val['Growth & Valuation'] == 'Market Capitalization', 'Growth & Valuation.1'].values[0]

# create a list and add the market capitalization to it
market_caps = [uba_market_cap]


for index, row in competitors.iterrows():
    competitors_ticker = row['Code']
    tickers.append(competitors_ticker)
    
    competitors_market_cap = row['M. Cap.']
    market_caps.append(competitors_market_cap)

# method to convert market cap to actual numbers
def convert_market_cap(value):
    suffixes = {'B': 1e9, 'T': 1e12}
    suffix = value[-1]
    if suffix in suffixes:
        return float(value[:-1]) * suffixes[suffix]
    else:
        return float(value)

market_caps_numerics = [convert_market_cap(value) for value in market_caps]

X_axis = np.arange(len(tickers)) 
bars = plt.bar(X_axis, market_caps_numerics, width=0.7, label="Market Cap")
bars[0].set_color('#FF5733')
for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), market_caps[i], ha='center', va='bottom')


plt.xticks(X_axis, tickers)
plt.xlabel("Companies") 
plt.ylabel("Market Cap")
plt.title("UBA vs Competitors' Market Cap") 
plt.show()