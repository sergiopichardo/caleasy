# import datetime
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class AuthService:
    # Google Calendar API scopes and file names for credentials and token
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    CREDENTIALS_FILE_NAME = "credentials.json"
    TOKEN_FILE_NAME = "token.json"

    def __init__(self):
        """Initialize the AuthService and attempt to load saved credentials"""
        self.credentials = None
        try:
            self.credentials = self._load_credentials()
        except Exception as e:
            print(f"Failed to load credentials: {e}")

    def _load_credentials(self):
        """Load credentials from the token file if it exists"""
        try:
            if os.path.exists(self.TOKEN_FILE_NAME):
                return Credentials.from_authorized_user_file(self.TOKEN_FILE_NAME, self.SCOPES)
        except FileNotFoundError:
            print(f"Token file {self.TOKEN_FILE_NAME} not found.")
        except Exception as e:
            print(f"An error occurred while loading credentials: {e}")
        return None

    def _save_credentials(self):
        """Save the credentials to the token file"""
        try:
            with open(self.TOKEN_FILE_NAME, "w") as token:
                token.write(self.credentials.to_json())
        except Exception as e:
            print(f"Failed to save credentials to {self.TOKEN_FILE_NAME}: {e}")

    def _refresh_credentials(self):
        """Refresh the credentials if they are expired and a refresh token is available"""
        try:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
        except Exception as e:
            print(f"Failed to refresh credentials: {e}")

    def _run_auth_flow(self):
        """Run the authentication flow to obtain new credentials"""
        try:
            flow = InstalledAppFlow.from_client_secrets_file(self.CREDENTIALS_FILE_NAME, self.SCOPES)
            return flow.run_local_server(port=0)
        except FileNotFoundError:
            print(f"Credentials file {self.CREDENTIALS_FILE_NAME} not found.")
        except Exception as e:
            print(f"An error occurred during the authentication flow: {e}")

    def _authenticate(self):
        """Authenticate the user, refreshing credentials if necessary, or running the auth flow"""
        try:
            if not self.credentials or not self.credentials.valid:
                if self.credentials:
                    self._refresh_credentials()
                else:
                    self.credentials = self._run_auth_flow()
                if self.credentials:
                    self._save_credentials()
        except Exception as e:
            print(f"An error occurred during authentication: {e}")

    def get_authenticated_service(self):
        """Get an authenticated Google Calendar service object"""
        try:
            self._authenticate()
            return build("calendar", "v3", credentials=self.credentials)
        except HttpError as error:
            print(f"An error occurred with the Google Calendar API: {error}")
        except Exception as e:
            print(f"An error occurred while getting the authenticated service: {e}")
