import datetime
from googleapiclient.errors import HttpError

from services.authentication.auth import AuthService

def main():
    
    try:
        auth_service = AuthService()
        service = auth_service.get_authenticated_service()
        
        now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])
        
    except HttpError as error:
        print(f"An error occurred: {error}")
        

main()

# import datetime
# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/calendar"]

# CREDENTIALS_FILE_NAME = "credentials.json"
# TOKEN_FILE_NAME = "token.json"


# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists(TOKEN_FILE_NAME):
#         # Creates a Credentials instance from an authorized user json file.
#         creds = Credentials.from_authorized_user_file(TOKEN_FILE_NAME, SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE_NAME, SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open(TOKEN_FILE_NAME, "w") as token:
#             token.write(creds.to_json())

#     try:
#         service = build("calendar", "v3", credentials=creds)

        # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        # print("Getting the upcoming 10 events")
        # events_result = (
        #     service.events()
        #     .list(
        #         calendarId="primary",
        #         timeMin=now,
        #         maxResults=10,
        #         singleEvents=True,
        #         orderBy="startTime",
        #     )
        #     .execute()
        # )
        # events = events_result.get("items", [])

        # if not events:
        #     print("No upcoming events found.")
        #     return

        # # Prints the start and name of the next 10 events
        # for event in events:
        #     start = event["start"].get("dateTime", event["start"].get("date"))
        #     print(start, event["summary"])

#     except HttpError as error:
#         print(f"An error occurred: {error}")


# if __name__ == "__main__":
#     main()
