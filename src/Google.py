import json
import requests
from requests.api import delete
headers = {"Authorization": "Bearer ya29.a0AfH6SMBA5TgYao98_KzE8eNEMyjivfd32dPVtzt0krWYxTxVCgsKT5qzJQFMypp7bbSw5jOg8RA_yHdKW1HL455pbL6JT8CDKnymTn-g0SKDDCV4IvU9dNNBDhmBk_xQ96jDZoe9rARnqoccs2cRMoHn2hBy"}
para = {
    "name": "sample2.xlsx",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("/Users/normancade/Desktop/Robinhood-Webscraper.xlsx", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print("added")

p = requests.delete(
    "https://www.googleapis.com/drive/v3/files/" + "1kjWWrUiE6xxVivTXcJA1eavcMvQ2Ei5I",
    headers=headers,
)

print("deleted")

# requests.delete(
#     "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",

# )

print(r.text)

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
# drive = GoogleDrive(gauth)

# fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
# for file in fileList:
#   print('Title: %s, ID: %s' % (file['title'], file['id']))
#   # Get the folder ID that you want
#   if(file['title'] == "Stocks"):
#       fileID = file['id']

# file1 = drive.CreateFile({"mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
# file1.SetContentFile("small_file.csv")
# file1.Upload() # Upload the file.
# print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   



