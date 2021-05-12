import gspread
from oauth2client.service_account import ServiceAccountCredentials

def open_worksheet(sheetName) :
    scope = ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name("robinhood-webscraper-key.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open(sheetName).sheet1
    return sheet

def populate_table (sheet, collected_stock_info) :
    rowNum = 2
    sheet.delete_rows(rowNum, (len(collected_stock_info) + rowNum))
    print("Rows cleared")

    for stock in collected_stock_info :
        insertRow = [stock.symbol, stock.price, stock.closing_price, stock.sector, stock.fifty_day_avg, stock.twohundred_day_avg]
        sheet.insert_row(insertRow,rowNum)
        _pick_cell_color(rowNum, stock, sheet)
        rowNum = rowNum + 1
    print("Rows updated")


# ------------ Helper Functions ---------------

def _pick_cell_color(rowNum, stock, sheet) :
    if stock.fifty_day_avg > stock.price :
        sheet.format("E" + str(rowNum), {
            "backgroundColor": {
            "red": 1.0,
        }}) 
    else :
        sheet.format("E" + str(rowNum), {
            "backgroundColor": {
            "green": 1.0,
        }})
    if stock.twohundred_day_avg > stock.price :
        sheet.format("F" + str(rowNum), {
            "backgroundColor": {
            "red": 1.0,
        }}) 
    else :
        sheet.format("F" + str(rowNum), {
            "backgroundColor": {
            "green": 1.0,
        }})
