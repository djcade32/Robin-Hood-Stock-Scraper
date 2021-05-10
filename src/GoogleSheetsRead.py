# from googleapiclient.discovery import build
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials

# from google.oauth2 import service_account



# SERVICE_ACCOUNT_FILE = 'robinhood-webscraper-key.json'
# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheetsx']

# creds = None
# creds = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1Xwj9NncIAYKxUUaKfbr3xKfjJ30TME_MCZOzZkU4TSo'


    


# service = build('sheets', 'v4', credentials=creds)

# # Call the Sheets API
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="Sheet1!A1:C4").execute()
# # values = result.get('values', [])
# print(result)

# # if not values:
# #     print('No data found.')
# # else:
# #     print('Name, Major:')
# #     for row in values:
# #         # Print columns A and E, which correspond to indices 0 and 4.
# #         print('%s, %s' % (row[0], row[4]))

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("robinhood-webscraper-key.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Robinhood-Webscraper").sheet1

data = sheet.get_all_records()

print(data)