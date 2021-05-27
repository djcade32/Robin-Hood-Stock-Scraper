import os
from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = "client_secret_GoogleCloudDemo.json"
API_NAME = "drive"
API_VERSION = "v3"

SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def convert_excel_file(file_path: str, folder_ids: list=None) :
    if not os.path.exists(file_path) :
        print(f'{file_path} not found')
        return

    try :
        file_metadata = {
            'name': os.path.splitext(os.path.basename(file_path))[0],
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents' : folder_ids
        }

        media = MediaFileUpload(
            filename=file_path,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

        response = service.files().create(
            media_body=media,
            body=file_metadata
        ).execute()

        print(response)
        return response
    except Exception as ex :
        print(ex)
        return

excel_files = os.listdir('./Excel Files')

for excel_file in excel_files :
    convert_excel_file(os.path.join('./Excel Files', excel_file)), []