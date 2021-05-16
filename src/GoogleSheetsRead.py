from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# Format rule for currency
FORMAT_CURRENCY_USD_SIMPLE = '"$"#,##0.00_-'

    
# This populates the given google sheet with the given stock info
def populate_table (workbookPath, collected_stock_info) :
    # Loading workbook and making first sheet active
    try :
        wb = load_workbook(workbookPath)
        ws = wb.active
    except :
        print("Error: Cannot open workbook")
    # Clearing the sheet
    startRowNum = 2
    amountOfStocks = len(collected_stock_info)
    try :
        ws.delete_rows(startRowNum, amountOfStocks  + 1)
        print("Table Cleared")

        for stock in collected_stock_info :
            insertRow = [stock.symbol, 
                        stock.sector, 
                        stock.price, 
                        stock.average_buy_price, 
                        stock.quantity, 
                        stock.amount_spent, 
                        stock.closing_price, 
                        stock.fifty_day_avg, 
                        stock.twohundred_day_avg
                        ]
            ws.append(insertRow)
            _pick_cell_color(startRowNum, len(insertRow), stock, ws)
            startRowNum = startRowNum + 1
        print("Rows updated")

        # Format range of cells to be currency
        range1 = ws["C2" : "D" + str(len(collected_stock_info) + 1)]
        range2 = ws["F2" : "I" + str(len(collected_stock_info) + 1)]
        _format_cells(range1, format=FORMAT_CURRENCY_USD_SIMPLE)
        _format_cells(range2, format=FORMAT_CURRENCY_USD_SIMPLE)
    
        wb.save(r"C:\Users\Dj\Desktop\Robinhood-Webscraper.xlsx")
    except :
        print("Error: Cannot populate table")


# ------------ Helper Functions ---------------

# Formats the given range of cells with the given format rule
def _format_cells(range, format) :
    for cellTuple in range :
        for cell in cellTuple :
            cell.number_format = format

# Determines the color of the cell based off of the stocks 50
# and 200 day moving avg
def _pick_cell_color(rowNum, columnNum, stock, sheet) :
    if stock.fifty_day_avg > stock.price :
        sheet.cell(row=rowNum, column=columnNum-1).style = "Bad"
    else :
        sheet.cell(row=rowNum, column=columnNum-1).style = "Good"
    if stock.twohundred_day_avg > stock.price :
        sheet.cell(row=rowNum, column=columnNum).style = "Bad"
    else :
        sheet.cell(row=rowNum, column=columnNum).style = "Good"
