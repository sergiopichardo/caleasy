from typing import List, Dict, Any
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
