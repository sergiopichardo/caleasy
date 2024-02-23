import typer
from typing_extensions import Annotated

app = typer.Typer()

TODAYS_EVENTS_LIST = """
----- Thursday, February 22nd, 2024 -----
08:00am - 08:50am       Gym (Chest + Triceps)
09:00am - 09:50am       Algorithms (Linked Lists)  
11:00am - 11:30am       caleasy (create first CLI UI outline)
12:01pm - 12:20pm       Lunch
01:15pm - 01:45pm       Go out for a walk
04:00pm - 05:00pm       Meeting with Fulano De Tal
"""

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


@app.command()
def list(
    week: Annotated[
        bool, typer.Option(
            "--week", 
            help="List all events for the current week"
        )
    ] = False
):
    """
    Displays a list of today's events from all calendars

    If --week is used, it lists all events for the week.
    """
    if week:
        print(WEEKLY_EVENTS_LIST)
    else:
        print(TODAYS_EVENTS_LIST)


if __name__ == "__main__":
    app()
