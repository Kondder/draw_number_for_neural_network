from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.colab import drive

# Monta Google Drive
drive.mount('/content/drive')

# Configura la API de Google Drive
drive_service = build('drive', 'v3')

# Ruta local al archivo CSV
file_path = '/set5/test_number_rz.pong'

# Ruta en Google Drive donde deseas guardar el archivo
drive_folder = '/content/drive/MyDrive/Image'

# Carga el archivo al servidor de Google Drive
media = MediaFileUpload(file_path, resumable=True)
file = drive_service.files().create(media_body=media, body={'name': 'output.csv', 'parents': [drive_folder]}).execute()
