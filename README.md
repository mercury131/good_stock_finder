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
4. pip install openpyxl

Or you can use portable version of Good stock finder for Windows [here](https://github.com/mercury131/good_stock_finder/releases/download/1.0/good_stock_finder.exe)

Then open directory with good_stock_finder.py and run it!

`
python good_stock_finder.py`

The program will show the found stocks:

`
Processing ticker -  TJX
Processing ticker -  TFC
Processing ticker -  UAA
Processing ticker -  VIAC
Processing ticker -  WAB
Processing ticker -  WRK
Processing ticker -  WY
Processing ticker -  WMB
Processing ticker -  ZION
   Ticker  Price  Quickratio  Current Ratio  Debt/Eq  Sales Q/Q  Gross Margin  Profit Margin   ROE              Sector
0     AMD  92.79         1.7            2.3     0.00       55.5          44.5           10.2  27.0          Technology
4     BWA  42.80         2.0            2.3     0.60        1.7          19.1            4.1   7.7   Consumer Cyclical
16    GLW  37.60         1.4            2.1     0.78        2.3          29.5            1.8   1.9          Technology
25     EW  85.52         2.6            3.5     0.14        4.3          75.5           18.2  19.7          Healthcare
27   EXPD  93.77         2.3            2.3     0.00       18.8          30.5            7.1  28.6         Industrials
28   FAST  47.72         2.2            4.4     0.14        2.5          45.8           15.1  30.6         Industrials
39     IR  45.23         1.7            2.4     0.44      123.8          32.8            4.0   2.3         Industrials
42   JNPR  25.04         1.9            2.0     0.00        0.5          58.1            8.9   8.8          Technology
48   MXIM  93.62         4.7            5.3     0.58       16.2          66.1           30.0  40.7          Technology
53   MNST  88.20         3.2            3.7     0.00       10.0          58.3           27.0  28.2  Consumer Defensive
67    UAA  18.51         1.3            2.1     0.00        0.2          47.6           16.6  45.4   Consumer Cyclical
70     WY  33.21         2.0            2.5     0.70       26.3          23.7            7.0   6.0         Real Estate`

The program also exports data to a CSV and Excel files in current directory.
