import robin_stocks.robinhood as rb
import pyotp
import GetStockInfo
import GoogleSheetsRead
import yaml

# Get neccessary credentials
conf = yaml.load(open('credentials.yml'), Loader=yaml.FullLoader)
email = conf['user']['email']
pwd = conf['user']['password']
key = conf['user']['key']

def main():

    try :
        # Login into Robinhood
        totp = pyotp.TOTP(key).now()
        login = rb.login(email, pwd, mfa_code=totp)
    except :
        print("Error: Cannot log into to Robinhood")

    myStocks = GetStockInfo.build_portfolio()
    collected_stock_info = GetStockInfo.collect_stock_info(myStocks)
    GoogleSheetsRead.populate_table(r"C:\Users\Dj\Desktop\Robinhood-Webscraper.xlsx", collected_stock_info)


if __name__ == "__main__":
    main()

    
