import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("robinhood-webscraper-key.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Robinhood-Webscraper").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)
col = sheet.col_values(2)
cell = sheet.cell(1,2).value

# insertRow = ["hello", 5, "red", "blue"]
# sheet.insert_row(insertRow, 4)
# sheet.delete_row(4)
# sheet.update_cell(2, 2, "Changed")

numRows = len(data)

print(numRows)
