from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Definir los permisos (alcances)
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

# Iniciar el flujo de autenticación
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
creds = flow.run_local_server(port=0)

# Imprimir los tokens
print("Access Token:", creds.token)
print("Refresh Token:", creds.refresh_token)
print("Client ID:", creds.client_id)
print("Client Secret:", creds.client_secret)
