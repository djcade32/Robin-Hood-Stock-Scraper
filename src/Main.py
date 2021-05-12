import robin_stocks.robinhood as rb
import pyotp
import sys
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import GetStockInfo
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yaml

# Get neccessary credentials
conf = yaml.load(open('credentials.yml'), Loader=yaml.FullLoader)
email = conf['user']['email']
pwd = conf['user']['password']
key = conf['user']['key']


today = date.today()

try :
    # Login into Robinhood
    totp = pyotp.TOTP(key).now()
    login = rb.login(email, pwd, mfa_code=totp)
except :
    print("Error logging into to Robinhood")

myStocks = GetStockInfo.build_portfolio()
collected_stock_info = GetStockInfo.collect_stock_info(myStocks)

scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("robinhood-webscraper-key.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Robinhood-Webscraper").sheet1

data = sheet.get_all_records()






rowNum = 2
sheet.delete_rows(rowNum, (len(collected_stock_info) + rowNum))
print("Rows cleared")

for stock in collected_stock_info :
    insertRow = [stock.symbol, stock.price, stock.closing_price, stock.sector, stock.fifty_day_avg, stock.twohundred_day_avg]
    sheet.insert_row(insertRow,rowNum)
    rowNum = rowNum + 1
print("Rows updated")



# dateList = stocks["stock_previous_close_dates"][0].split("-")
# stringToDate = date(int(dateList[0]), int(dateList[1]), int(dateList[2]))

# if stringToDate < today :
#     print(True)
# else :
#     print(False)
    
