from services.auth_service import AuthService
# from event import EventService
from calendar import CalendarService

def main():
    
    try:
        auth_service = AuthService()
        # event_service = EventService(auth_service)
        calendar_service = CalendarService(auth_service)

        calendars = calendar_service.list_all_calendars()
        
        for calendar in calendars:
            print(calendar, '\n')
            if calendar['primary']:
                print(f"[PRIMARY] {calendar['summary']}")
            else:
                print(calendar['summary'])

    except Exception as error:
        print(f"An error occurred: {error}")
        

if __name__ == "__main__":
    main()
