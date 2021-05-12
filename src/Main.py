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
import GoogleSheetsRead
import yaml

# Get neccessary credentials
conf = yaml.load(open('credentials.yml'), Loader=yaml.FullLoader)
email = conf['user']['email']
pwd = conf['user']['password']
key = conf['user']['key']

def main():
    today = date.today()

    try :
        # Login into Robinhood
        totp = pyotp.TOTP(key).now()
        login = rb.login(email, pwd, mfa_code=totp)
    except :
        print("Error logging into to Robinhood")

    myStocks = GetStockInfo.build_portfolio()
    collected_stock_info = GetStockInfo.collect_stock_info(myStocks)
    sheet = GoogleSheetsRead.open_worksheet("Robinhood-Webscraper")
    GoogleSheetsRead.populate_table(sheet, collected_stock_info)


if __name__ == "__main__":
    main()

# dateList = stocks["stock_previous_close_dates"][0].split("-")
# stringToDate = date(int(dateList[0]), int(dateList[1]), int(dateList[2]))

# if stringToDate < today :
#     print(True)
# else :
#     print(False)
    
