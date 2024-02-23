from services.auth_service import AuthService


from googleapiclient.errors import HttpError


class CalendarService:
    def __init__(self, auth_service: AuthService) -> None:
        self.service = auth_service.get_authenticated_service()

    def list_all_calendars(self):
        events_result = self.service.calendarList().list().execute()
        calendars = events_result.get("items", [])
        return calendars 