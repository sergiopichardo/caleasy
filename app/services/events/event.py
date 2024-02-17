import datetime 
from googleapiclient.errors import HttpError
from services.authentication.auth import AuthService

class EventService:
    def __init__(self, auth_service: AuthService) -> None:
        """
        Initializes the EventService with an AuthService instance.

        This service is responsible for fetching and managing events from the Google Calendar API.

        :param auth_service: An instance of AuthService for authenticated Google API operations.
        """
        self.service = auth_service.get_authenticated_service()

    def list_upcoming_events(self, num_events=10):
        """
        Lists the upcoming events from the user's primary Google Calendar.

        Prints the start time and summary of each upcoming event to the console. If no upcoming events are found,
        a message indicating this will be printed.

        :param num_events: The maximum number of events to retrieve (default is 10).
        """
        try: 
            now = datetime.datetime.utcnow().isoformat() + "Z" # 'Z' indicates UTC time
            print("getting the upcoming events")
            events_result = self.service.events().list(
                calendarId="primary",
                timeMin=now,
                maxResults=num_events,
                singleEvents=True,
                orderBy="startTime"
            ).execute()

            events = events_result.get("items", [])

            if not events:
                print("No upcoming events found.")
            else: 
                for event in events:
                    start = event["start"].get("dateTime", event["start"].get("date"))
                    print(start, event.get("summary"))

        except HttpError as error:
            print(f"An error ocurred listing upcoming events: {error}")