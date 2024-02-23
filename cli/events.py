import typer 

app = typer.Typer()

@app.command()
def events():
    """
    Displays a list of today's events from all calendars
    """
    stub_text = """
----- Thursday, February 22nd, 2024 -----
08:00am - 08:50am       Gym (Chest + Triceps)
09:00am - 09:50am       Algorithms (Linked Lists)  
11:00am - 11:30am       caleasy (create first CLI UI outline)
12:01pm - 12:20pm       Lunch
01:15pm - 01:45pm       Go out for a walk
04:00pm - 05:00pm       Meeting with Fulano De Tal
"""
    print(stub_text)
