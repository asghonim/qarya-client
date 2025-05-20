import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import os

def upload_sheet():
    # Check if the private.key file exists
    if not os.path.isfile("private.key"):
        raise FileNotFoundError("private.key file not found. Please ensure the file exists in the current directory.")

    # The URL of your Cloud Run service
    url = "https://upload-sheet-205247550303.europe-west3.run.app"

    # Read the private key from the file
    with open("private.key", "r") as key_file:
        private_key = key_file.read()

    SERVICE_ACCOUNT_INFO = {
        "type": "service_account",
        "project_id": "tazaker-e359d",
        "private_key_id": "4af494e65fc5b49141b56b14e3c78cd5c0a8d732",
        "private_key": private_key,
        "client_email": "qarya-client-1@tazaker-e359d.iam.gserviceaccount.com",
        "client_id": "100081783763521161824",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/qarya-client-1%40tazaker-e359d.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }

    target_audience = url

    # Create credentials from the service account info
    credentials = service_account.IDTokenCredentials.from_service_account_info(
        SERVICE_ACCOUNT_INFO,
        target_audience=target_audience
    )

    # Refresh to get the token
    auth_req = Request()
    credentials.refresh(auth_req)

    # Make the authenticated request
    headers = {"Authorization": f"Bearer {credentials.token}"}
    response = requests.get(url, headers=headers)

    print("Status code:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    upload_sheet()