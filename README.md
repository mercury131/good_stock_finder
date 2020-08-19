# Good Stock Finder
This program is not an individual investment recommendation and cannot be used as a robot advisor.

This program search not bad stocks from S&P 500 Index.

# How does search work?
The program selects stocks according to the following parameters:
1. The company has sales revenue for the last quarter
2. The company has no big debts
3. The Quick / Current ratio is not overheated
4. Good ROE/Gross Margin/Profit Margin

# How to use it?

First install python 3 and this components via pip:
1. yum install python36 (Centos) or apt install python3 (Debian\Ubuntu) or get installer for Windows [here](https://www.python.org/downloads/windows/)
2. pip install pandas
3. pip install finviz

Then open directory with good_stock_finder.py and run it!

`
python good_stock_finder.py`

The program will show the found stocks:

`
Processing ticker -  WMT
Processing ticker -  WY
Processing ticker -  WMB
Processing ticker -  XEL
Processing ticker -  XLNX
Processing ticker -  ZBRA
Processing ticker -  ZTS
Found Good Tickers -  ['ABT', 'ATVI', 'AMD', 'AAP', 'APD', 'AKAM', 'ALB', 'ARE', 'ALGN', 'GOOGL', 'AEE', 'AWK', 'ABC', 'APH', 'ADI', 'ANTM', 'AOS', 'AMAT', 'APTV', 'ADM', 'AJG', 'BIO', 'BLK', 'BWA', 'BMY', 'BR', 'CHRW', 'CDNS', 'CLX', 'CTSH', 'CPRT', 'GLW', 'COST', 'CSX', 'DVA', 'DXCM', 'DLR', 'DPZ', 'DOV', 'DRE', 'ETFC', 'ETN', 'EBAY', 'EW', 'EA', 'EQIX', 'EL', 'FB', 'FIS', 'FRC', 'FMC', 'FTV', 'FBHS', 'GIS', 'HOLX', 'IDXX', 'ITW', 'IR', 'IQV', 'JNJ', 'JCI', 'KSU', 'K', 'KEYS', 'KLAC', 'LH', 'LRCX', 'LEN', 'MKTX', 'MMC', 'MA', 'MXIM', 'MCHP', 'MSFT', 'MDLZ', 'MCO', 'MS', 'MSCI', 'NDAQ', 'NEM', 'NSC', 'NVR', 'ORLY', 'ORCL', 'PCAR', 'PH', 'PYPL', 'PNR', 'PKI', 'PFE', 'PG', 'PGR', 'PLD', 'PHM', 'QCOM', 'REGN', 'RHI', 'ROP', 'CRM', 'SBAC', 'NOW', 'SWKS', 'SWK', 'STE', 'SIVB', 'SNPS', 'TROW', 'TTWO', 'TFX', 'TIF', 'TT', 'UNP', 'UNH', 'VAR', 'VRSN', 'VRSK', 'VZ', 'V', 'WMT', 'WY', 'WMB', 'XEL', 'XLNX', 'ZBRA', 'ZTS']
Found Hot Tickers -  []`

The program also exports data to a CSV files in current directory.
