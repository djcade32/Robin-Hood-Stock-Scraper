import robin_stocks.robinhood as rb
import pyotp
import sys
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from collections import namedtuple


def build_portfolio () :
    # Get my portfolio info
    my_stocks = rb.build_holdings()
    myStocks = my_stocks.items()
    return myStocks

def collect_stock_info (myStocks) :
    # This is created to hold all of the created tuples for my stocks
    collected_stock_info = []

    # This is creating a tuple for one stock
    CurStock = namedtuple("CurStock", ["symbol", "price", "closing_price", "previous_close_date", "sector", "fifty_day_avg", "twohundred_day_avg"])

    # This will iterate through all of my stocks, grab the needed data and create a tuple for each stock
    for stock in myStocks :
        # Grabbing the neccessary data
        curSymbol = rb.get_quotes(stock, info="symbol")[0]
        curStockPrice = float(rb.stocks.get_latest_price(stock)[0])
        curPreviousClose = float(rb.get_quotes(stock, info="previous_close")[0])
        curPreviousCloseDate = rb.get_quotes(stock, info="previous_close_date")[0]
        curStockSector = rb.stocks.get_fundamentals(stock, info="sector")[0]
        curStock50DayAvg = "none"
        curStock200DayAvg = "none"

        # This is getting the 50 Day and 200 Day moving Avg
        # If there is an error it will try to use a different website to get the needed info
        try :
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
            html = "https://financhill.com/stock-price-chart/" + curSymbol + "-technical-analysis"
            html_text = requests.get(html, headers = headers)
            soup = BeautifulSoup(html_text.text, "lxml")
            prevTd = soup.find("td", string = "50-day Simple Moving Average:")
            curStock50DayAvg = float(prevTd.find_next_sibling("td").text)
            prevTd = soup.find("td", string = "200-day Simple Moving Average:")
            curStock200DayAvg = float(prevTd.find_next_sibling("td").text)
        except :
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
            html = "https://stockanalysis.com/stocks/" + curSymbol + "/statistics/"
            html_text = requests.get(html, headers = headers)
            soup = BeautifulSoup(html_text.text, "lxml")
            prevTd = soup.find("span", string = "50-Day Moving Average")
            curStock50DayAvg = float(prevTd.find_next("td").text)
            prevTd = soup.find("td", string = "200-Day Moving Average")
            curStock200DayAvg = float(prevTd.find_next("td").text)

        # if curStock50DayAvg != "none" :
        #     if curStock50DayAvg > curStockPrice :
        #         print("Below 50 Day Avg")
        #     else :
        #         print("Above 50 Day Avg")
        # else :
        #     print("none")

        # if curStock200DayAvg != "none" :
        #     if curStock200DayAvg > curStockPrice :
        #         print("Below 200 Day Avg")
        #     else :
        #         print("Above 200 Day Avg")
        # else :
        #     print("none")

        curStock = CurStock(symbol = curSymbol, price = curStockPrice, closing_price = curPreviousClose, previous_close_date = curPreviousCloseDate, sector = curStockSector, fifty_day_avg = curStock50DayAvg, twohundred_day_avg = curStock200DayAvg)
        
        # Add created stock tuple to the collection of all stock tuples
        collected_stock_info.append(curStock)
        
    return collected_stock_info