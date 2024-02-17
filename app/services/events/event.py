import datetime 
from googleapiclient.error import HttpError
from services.authentication.auth import AuthService

class EventService:
    def __init__(self, auth_service: AuthService) -> None:
        """
        Initializes the EventService with an AuthService instance.

        This service is responsible for fetching and managing events from the Google Calendar API.

        :param auth_service: An instance of AuthService for authenticated Google API operations.
        """
        self.service = auth_service.get_authenticated_service()
