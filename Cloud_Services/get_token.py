import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request

# Cargar el archivo credentials.json
CLIENT_SECRET_FILE = 'credentials.json'  # Ruta a tu archivo credentials.json
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_credentials():
    creds = None
    # El archivo token.pickle almacena el token de acceso y refresco
    # y es creado automáticamente cuando el flujo de autorización se completa por primera vez.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Si no hay credenciales válidas disponibles, deja que el usuario inicie sesión
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Guardar las credenciales para la próxima vez
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def main():
    creds = get_credentials()
    
    # Llamar a la API de Google Drive
    service = googleapiclient.discovery.build(API_NAME, API_VERSION, credentials=creds)
    
    # Realizar una prueba, listando los archivos en Google Drive
    results = service.files().list(pageSize=10, fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(f'{item["name"]} ({item["id"]})')

    # Imprimir el access token
    print("Access Token:", creds.token)

if __name__ == '__main__':
    main()
