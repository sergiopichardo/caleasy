import typer 
from cli.events import app as events_app

app = typer.Typer()
app.add_typer(events_app, name="events")


if __name__ == "__main__":
    app()
