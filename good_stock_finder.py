print("Start Search..")

import pandas as pd

import csv

import os

from finviz.screener import Screener
import finviz

setprice = input('Do you want set max price for ticker? (Y\\N): ') 

if setprice == "Y"  :
    maxprice = float(input("Enter max $ price value: ") )
    print("Set max price to:", maxprice) 
elif setprice == "y"  :
    maxprice = float(input("Enter max price value: ") )
    print("Set max price to:", maxprice)
else :
    print("Max price not set..")

# There are 2 tables on the Wikipedia page
# we want the first table

payload=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]

df = first_table

symbols = df['Symbol'].values.tolist()

#print(symbols)

found_tickers = []
    
for ticker in symbols :
    print("Get data for ticker - ", ticker)
    curprice = float((finviz.get_stock(ticker.replace(".","-"))['Price']))
    range52 = (finviz.get_stock(ticker.replace(".","-"))['52W Range'])
    low52 = float((range52.split('-')[0].strip()))
    high52 = float((range52.split('-')[1].strip()))
    try:
        ticker_radar = round((high52 - low52) / (high52 - curprice))
    except ZeroDivisionError:
        ticker_radar = 0
    if (ticker_radar > 4) and (ticker_radar < 30) :
        try:
            if curprice > maxprice :
                print("Skip, Ticker by price - ", ticker)
            else:
                found_tickers.append(ticker)
        except NameError:
            found_tickers.append(ticker)



good_tickers = []
hot_tickers = []



for ticker in found_tickers :
    print("Processing ticker - ", ticker)
    try:
        quickratio = float((finviz.get_stock(ticker.replace(".","-"))['Quick Ratio']))
    except ValueError:
        quickratio = 5
    try:
        currentratio = float((finviz.get_stock(ticker.replace(".","-"))['Current Ratio']))
    except ValueError:
        currentratio = 5
    try:
        debteq = float((finviz.get_stock(ticker.replace(".","-"))['Debt/Eq']))
    except ValueError:
        debteq = 100
    try:
        salesqq = float((finviz.get_stock(ticker.replace(".","-"))['Sales Q/Q']).replace("%",""))
    except ValueError:
        salesqq = 0
    try:
        grossmargin = float((finviz.get_stock(ticker.replace(".","-"))['Gross Margin']).replace("%",""))
    except ValueError:
        grossmargin = 0
    try:
        profitmargin = float((finviz.get_stock(ticker.replace(".","-"))['Profit Margin']).replace("%",""))
    except ValueError:
        profitmargin = 0
    try:
        roe = float((finviz.get_stock(ticker.replace(".","-"))['ROE']).replace("%",""))
    except ValueError:
        roe = 0
    if (quickratio < 1) :
        quickratio = 2
    elif (quickratio > 2) :
        quickratio = 3
    elif (quickratio > 1) :
        quickratio = 5

    if (currentratio < 2) :
        currentratio = 3
    elif (currentratio < 1) :
        currentratio = 2
    elif (currentratio > 2) :
        currentratio = 5

    if (debteq <= 1) :
        debteq = 5
    elif (debteq > 2) :
        debteq = 2
    elif (debteq < 2) :
        debteq = 3

    if (salesqq > 0.1) :
        salesqq = 5
    elif (salesqq < 0) :
        salesqq = 2
    elif (salesqq == 0) :
        salesqq = 3
    elif (salesqq > 0) :
        salesqq = 4

    if (grossmargin > 0.4) :
        grossmargin = 5
    elif (grossmargin < 0.1) :
        grossmargin = 2
    elif (grossmargin == 0) :
        grossmargin = 1
    elif (grossmargin > 0.3) :
        grossmargin = 4

    if (profitmargin > 0.4) :
        profitmargin = 5
    elif (profitmargin < 0.1) :
        profitmargin = 2
    elif (profitmargin == 0) :
        profitmargin = 1
    elif (profitmargin < 0.3) :
        profitmargin = 3
    elif (profitmargin > 0.3) :
        profitmargin = 4

    if (roe > 0.5) :
        roe = 5
    elif (roe < 0.1) :
        roe = 2
    elif (roe == 0) :
        roe = 1
    elif (roe < 0.3) :
        roe = 3
    elif (roe > 0.3) :
        roe = 4
    finalresult = round(quickratio + currentratio + debteq + salesqq + grossmargin + profitmargin + roe)

    if (finalresult <= 24) :
        tempvar=0
    elif (finalresult > 24) :
        good_tickers.append(ticker)
    elif (finalresult > 30) :
        hot_tickers.append(ticker)


print("Found Good Tickers - ", good_tickers)

print("Found Hot Tickers - ", hot_tickers)

wtr = csv.writer(open ((os.path.dirname(os.path.realpath(__file__)) + '/good_tickers.csv'), 'w'), delimiter=';', lineterminator='\n')
wtr.writerow (['Ticker', 'Price', 'Quickratio', 'Current Ratio' , 'Debt/Eq' , 'Sales Q/Q', 'Gross Margin', 'Profit Margin', 'ROE', 'Sector'])
for x in good_tickers : wtr.writerow ([x  , (float((finviz.get_stock(x)['Price']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Quick Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Current Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Debt/Eq']))) , (str((finviz.get_stock(x.replace(".","-"))['Sales Q/Q']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Gross Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Profit Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['ROE']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Sector']).replace("%",""))) ])

wtr = csv.writer(open ((os.path.dirname(os.path.realpath(__file__)) + '/hot_tickers.csv'), 'w'), delimiter=';', lineterminator='\n')
wtr.writerow (['Ticker', 'Price', 'Quickratio', 'Current Ratio' , 'Debt/Eq' , 'Sales Q/Q', 'Gross Margin', 'Profit Margin', 'ROE', 'Sector'])
for x in hot_tickers : wtr.writerow ([x  , (float((finviz.get_stock(x)['Price']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Quick Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Current Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Debt/Eq']))) , (str((finviz.get_stock(x.replace(".","-"))['Sales Q/Q']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Gross Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Profit Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['ROE']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Sector']).replace("%",""))) ])
