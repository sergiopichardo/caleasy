import typer
import pendulum
from typing_extensions import Annotated
from services.auth_service import AuthService
from services.event_service import EventService
from services.calendar_service import CalendarService
from rich.console import Console
from rich.progress import Progress, SpinnerColumn

app = typer.Typer()

auth_service = AuthService


WEEKLY_EVENTS_LIST = """
Thu Feb 22      08:00am - 08:50am   Gym (Chest + Triceps)
                09:00am - 09:50am   Algorithms (Linked Lists)  
                11:00am - 11:30am   caleasy (create first CLI UI outline)
                12:01pm - 12:20pm   Lunch
                01:15pm - 01:45pm   Go out for a walk
                04:00pm - 05:00pm   Meeting with Fulano De Tal

Fri Feb 23      08:00am - 08:50am   Gym (Back + Arms)
                09:00am - 09:50am   Algorithms (Linked Lists)  
                11:00am - 11:30am   caleasy (add events stubs)
                12:01pm - 12:20pm   Lunch
                01:15pm - 01:45pm   Meeting with Juanes
                04:00pm - 05:00pm   caleasy (keep working on events)
...
"""

auth_service = AuthService()
event_service = EventService(auth_service)
console = Console()


@app.command()
def list(
    date: Annotated[
        str,
        typer.Option(
            "--date",
            help="List all events for a specific date in the format YYYY-MM-DD",
        ),
    ] = ""
):
    """
    Displays a list of events from all calendars

    If no value for --date is passed, it return all events from all calendars based on the current date.

    If --date is passed, it lists all events on that specific date.

    """
    # target_date = None
    if date != "":
        target_date = pendulum.parse(date)
    else:
        target_date = pendulum.now()

    # format date for heading
    formatted_date = target_date.format("dddd, MMMM DD, YYYY")


    with Progress("[progress.description]{task.description}", SpinnerColumn(), "{task.fields[status]}", console=console) as progress:
        # create new progress task
        task = progress.add_task("[cyan]Fetching events...", status="initializing")
        
        # get all calendars
        all_calendars = event_service.get_all_calendars()

        # update progress indicator with "fetching tasks"
        progress.update(task, advance=1, status="fetching calendars")

        # get all events
        all_events = event_service.get_events_from_calendars(all_calendars, target_date.to_date_string())

        # update progress indicator with "completed"
        progress.update(task, advance=1, status="completed")

    console.print(f"------ {formatted_date} -----")
    for event in all_events:
        start_time = event['start_datetime'].format('hh:mm A')
        end_time = event['end_datetime'].format('hh:mm A')
        event_summary = event['summary']
        calendar_summary = event['calendar_summary']
        console.print(f"{start_time} - {end_time}   {event_summary} ({calendar_summary})")


@app.command()
def create(
    title: Annotated[str, typer.Option(prompt=True)],
    description: Annotated[str, typer.Option(prompt=True)],
    start_time: Annotated[str, typer.Option(prompt=True)],
    end_time: Annotated[str, typer.Option(prompt=True)],
    attendees: Annotated[
        str,
        typer.Option(
            prompt="Enter attendees' emails (e.g. ana@email.com, bob@email.com)"
        ),
    ],
):
    print(f"title: {title}")
    print(f"description: {description}")
    print(f"time: {start_time} to {end_time}")
    print(f"attendees: {attendees}")


if __name__ == "__main__":
    app()
