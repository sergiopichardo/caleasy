from typing import List, Dict, Any

import pendulum
from googleapiclient.errors import HttpError
from services.auth_service import AuthService

class EventService:
    def __init__(self, auth_service: AuthService) -> None:
        """
        Initializes the EventService with an AuthService instance.

        This service is responsible for fetching and managing events from the Google Calendar API.

        :param auth_service: An instance of AuthService for authenticated Google API operations.
        """
        self.service = auth_service.get_authenticated_service()

    
    def get_all_calendars(self) -> List[Dict[str, Any]]:
        """
            Args: 
                None

            Returns:
                list: list of all calendars in a user's google's calendar account
        """
        try: 
            calendars_result = self.service.calendarList().list().execute()
            return calendars_result.get("items", [])
        except HttpError as error:
            print(f"An error ocurred fetching all calendars: {error}")

    def get_events_from_calendar(self, calendar: Dict[str, Any], date: str) -> List[Dict[str, Any]]:
        """
            Fetch all events for a specified calendar and date.

            Parameters:
                calendar: A dictionary containing the calendar ID and timezone.
                date: The target date for which to retrieve events, in 'YYYY-MM-DD' format. e.g. "2024-02-29

            Returns:
                A list of event dictionaries for the specified date.

            Raises:
                HttpError: it raises an HTTP error if an error ocurred while fetching the calendar events.
        """
        try:
            date_obj = pendulum.parse(date, tz=calendar['timeZone'])
            time_min = date_obj.start_of('day').to_rfc3339_string()
            time_max = date_obj.end_of('day').to_rfc3339_string()

            events_result = self.service.events().list(
                calendarId=calendar['id'],
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy='startTime',
            ).execute()

            return [
                {
                    'id': event['id'],
                    'summary': event['summary'],
                    'description': event.get('description', None),
                    'start_datetime': pendulum.parse(event['start']['dateTime']),
                    'end_datetime': pendulum.parse(event['end']['dateTime']),
                    'time_zone': event['start']['timeZone'],
                } 
                
                for event in events_result.get('items', [])
            ]

        except HttpError as error: 
            print(f"An error occurred while fetching events from an individual calendar: {error}")
            return []
