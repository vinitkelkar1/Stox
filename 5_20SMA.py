# This script will grab SMA for a Ticker from www.alphavantage.co
#Date: 11/28/2018
#Author : Vinit Kelkar
#Version : 1.0
# This is a hobby project from a beginner programmer. Suggestions are welcome.
# Enter list of stocks you want to run 5-20 SMA crossover algorithm for
stocks = ["WFC", "MSFT"]

import requests, json, csv, re


# This portion will get all timestamps which will help if market is closed over weekends or long weekends.
url = "https://www.alphavantage.co/query?function=SMA&symbol=" + stocks[0] + "&interval=daily&time_period=5&series_type=open&apikey=RJWUOJ73UGV1LOZE"
url_response = requests.get(url)
url_response_json = json.loads(url_response.text)

timestamps = list(url_response_json['Technical Analysis: SMA'].keys())

today = str(timestamps[0])


yesterday = timestamps[1]
parva = timestamps[2]
terva = timestamps[3]print(today)
# print(yesterday)
# print(parva)
print(terva)

## End of timestamps collection


# #Get Value of 5 Day SMA
for stock in stocks:
    print(stock)
    url = "https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=daily&time_period=5&series_type=close&apikey=FORILT2KP0D3QXR7"
   #  url = "https://www.alphavantage.co/query?function=SMA&symbol=" + stock + "&interval=daily&time_period=5&series_type=open&apikey=RJWUOJ73UGV1LOZE"
    response4 = requests.get(url)
    response5 = json.loads(response4.text)
    #print(type(response5))
    # print(response5)
    sma5_today = response5['Technical Analysis: SMA'][today]['SMA']
    sma5_yest = response5['Technical Analysis: SMA'][yesterday]['SMA']
    sma5_parva = response5['Technical Analysis: SMA'][parva]['SMA']
   # print(sma5_parva)
    print("sma5 today is", sma5_today)
    print("sma5 yest is ", sma5_yest)
    print("sma5 parva is", sma5_parva)
    #print(response5['Technical Analysis: SMA'])
    #print(response5['Technical Analysis: SMA'][yesterday]['SMA'])
    #print(type(response))

#
# #Get Value of 20 Day SMA
    url = "https://www.alphavantage.co/query?function=SMA&symbol=" + stock + "&interval=daily&time_period=20&series_type=close&apikey=FORILT2KP0D3QXR7"
    response19 = requests.get(url)
    response20 = json.loads(response19.text)
    sma20_today = response20['Technical Analysis: SMA'][today]['SMA']
    sma20_yest = response20['Technical Analysis: SMA'][yesterday]['SMA']
    sma20_parva = response20['Technical Analysis: SMA'][parva]['SMA']
    print("sma20 today is", sma20_today)
    print("sma20 yest is ", sma20_yest)
    print("sma20 parva is", sma20_parva)

    if (sma5_parva < sma20_parva and sma5_yest > sma20_yest) or (sma5_yest < sma20_yest and sma5_today > sma20_today):
        print("SMA 5-20 Crossover has happened for", stock)



