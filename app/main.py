from services.events.event import EventService
from services.authentication.auth import AuthService

def main():
    
    try:
        auth_service = AuthService()
        event_service = EventService(auth_service)

        event_service.list_upcoming_events(5)

    except Exception as error:
        print(f"An error occurred: {error}")
        

if __name__ == "__main__":
    main()
