from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '1cCwgWqTiBVxkwyoM6fv4xK5r3wISzMU2'
file_names = ['try.pdf', 'archive.zip']
mime_types = ['application/pdf', 'application/zip']

for file_name, mime_type in zip (file_names, mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload('./Yellowstone/{0}'.format(file_name), mimetype=mime_type)
    service.files().create(
      body = file_metadata,
      media_body = media,
      fields = 'id'
      ).execute()
