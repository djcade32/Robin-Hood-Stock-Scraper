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
workbookPath = conf['user']['workbookPath']


def main():

    try :
        # Login into Robinhood
        totp = pyotp.TOTP(key).now()
        rb.login(email, pwd, mfa_code=totp)
    except Exception as ex :
        print("Error: Cannot log into to Robinhood")
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    myStocks = GetStockInfo.build_portfolio()
    collected_stock_info = GetStockInfo.collect_stock_info(myStocks)
    GoogleSheetsRead.populate_table(workbookPath, collected_stock_info)


if __name__ == "__main__":
    main()

    
