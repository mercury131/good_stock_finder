print("Start Search..")

import pandas as pd

import csv

import os

import re

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

good_tickers = []
hot_tickers = []
tickers_radar = {}
tickers_rating = {}
    
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
                tickers_radar.update({ticker: ticker_radar})
        except NameError:
            found_tickers.append(ticker)
            tickers_radar.update({ticker: ticker_radar})






for ticker in found_tickers :
    ticker = ticker.replace(".","-")
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
        tickers_rating.update({ticker: finalresult})
    elif (finalresult > 30) :
        hot_tickers.append(ticker)
        tickers_rating.update({ticker: finalresult})


#print("Found Good Tickers - ", good_tickers)

#print("Found Hot Tickers - ", hot_tickers)

wtr = csv.writer(open ((os.path.dirname(os.path.realpath(__file__)) + '/good_tickers.csv'), 'w'), delimiter=';', lineterminator='\n')
wtr.writerow (['Ticker', 'Price', 'Quickratio', 'Current Ratio' , 'Debt/Eq' , 'Sales Q/Q', 'Gross Margin', 'Profit Margin', 'ROE', 'Sector', 'Radar', 'Rating'])
for x in good_tickers : wtr.writerow ([x  , (float((finviz.get_stock(x)['Price']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Quick Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Current Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Debt/Eq']))) , (str((finviz.get_stock(x.replace(".","-"))['Sales Q/Q']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Gross Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Profit Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['ROE']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Sector']).replace("%",""))) ,(str(tickers_radar[x])),(str(tickers_rating[x])) ])

wtr = csv.writer(open ((os.path.dirname(os.path.realpath(__file__)) + '/hot_tickers.csv'), 'w'), delimiter=';', lineterminator='\n')
wtr.writerow (['Ticker', 'Price', 'Quickratio', 'Current Ratio' , 'Debt/Eq' , 'Sales Q/Q', 'Gross Margin', 'Profit Margin', 'ROE', 'Sector', 'Radar', 'Rating'])
for x in hot_tickers : wtr.writerow ([x  , (float((finviz.get_stock(x)['Price']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Quick Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Current Ratio']))) , (str((finviz.get_stock(x.replace(".","-"))['Debt/Eq']))) , (str((finviz.get_stock(x.replace(".","-"))['Sales Q/Q']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Gross Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Profit Margin']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['ROE']).replace("%",""))) , (str((finviz.get_stock(x.replace(".","-"))['Sector']).replace("%",""))) ,(str(tickers_radar[x])),(str(tickers_rating[x])) ])

if good_tickers:
    excel_df = pd.read_csv('good_tickers.csv', 
                        sep=';'
                        )
    excel_df[:3]

    excel_df.to_excel('good_tickers.xlsx', index=False)
    
    print(excel_df)
    excel_df['Quickratio'] = excel_df['Quickratio'].replace('-','0').astype(float)
    excel_df['Current Ratio'] = excel_df['Current Ratio'].replace('-','0').astype(float)
    excel_df['Gross Margin'] = excel_df['Gross Margin'].replace('-','0').astype(float)
    excel_df['Profit Margin'] = excel_df['Profit Margin'].replace('-','0').astype(float)
    excel_df['ROE'] = excel_df['ROE'].replace('-','0').astype(float)
    excel_df['Debt/Eq'] = excel_df['Debt/Eq'].replace('-','0').astype(float)
    #excel_df['Sales Q/Q'] = excel_df['Sales Q/Q'].replace('-','0').astype(float)
    #print(excel_df)

    #filter=excel_df.loc[(excel_df['Quickratio'].astype(float)>=1) & (excel_df['Current Ratio'].astype(float)>=2) & (excel_df['Debt/Eq'].astype(float)<= 1) & (excel_df['Sales Q/Q'].astype(float)> 0.1) & (excel_df['Gross Margin'].astype(float)> 0.4) & (excel_df['Profit Margin'].astype(float)> 0.4) & (excel_df['ROE'].astype(float)> 0.5) ]
    filter=excel_df.loc[(excel_df['Quickratio']>=1) & (excel_df['Current Ratio']>=2) & (excel_df['Debt/Eq']<= 1) & (excel_df['Sales Q/Q']> 0.1) & (excel_df['Gross Margin']> 0.4) & (excel_df['Profit Margin']> 0.4) & (excel_df['ROE']> 0.5) ]

    filter.to_excel('good_tickers_filter.xlsx', index=False)
    print(filter)
if hot_tickers:
    excel_df = pd.read_csv('hot_tickers.csv', 
                        sep=';'
                        )
    excel_df[:3]

    excel_df.to_excel('hot_tickers.xlsx', index=False)

    excel_df['Quickratio'] = excel_df['Quickratio'].str.replace('-','0').astype(float)
    excel_df['Current Ratio'] = excel_df['Current Ratio'].str.replace('-','0').astype(float)
    excel_df['Gross Margin'] = excel_df['Gross Margin'].str.replace('-','0').astype(float)
    excel_df['Profit Margin'] = excel_df['Profit Margin'].str.replace('-','0').astype(float)
    excel_df['ROE'] = excel_df['ROE'].str.replace('-','0').astype(float)

    filter=excel_df.loc[(excel_df['Quickratio'].astype(float)>=1) & (excel_df['Current Ratio'].astype(float)>=2) & (excel_df['Debt/Eq'].astype(float)<= 1) & (excel_df['Sales Q/Q'].astype(float)> 0.1) & (excel_df['Gross Margin'].astype(float)> 0.4) & (excel_df['Profit Margin'].astype(float)> 0.4) & (excel_df['ROE'].astype(float)> 0.5) ]

    filter.to_excel('hot_tickers_filter.xlsx', index=False)
    print(filter)
