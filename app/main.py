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
        

if __name__ == "__main__":
    main()
    