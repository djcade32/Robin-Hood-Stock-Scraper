import json
import requests
from requests.api import delete
headers = {"Authorization": "Bearer ya29.a0AfH6SMC0WXdco4GAIsW0x7CdEN0z856iOF1aswOZpiUIvX0B-lxJ6vFmDqkwfOFgWKnc8W3WdwLjnz-Ju_CfkLqCY2uk3fVICC_7R1u91EUg263u0l71T7KfwTByvIfG1JbqDnElv_j37nMhJsj1M2Hh_Mo4"}
para = {
    "name": "sample.xlsx",
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

requests.delete(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",

)

print(r.text)