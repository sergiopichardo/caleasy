import typer 
import cli.events as events


app = typer.Typer()
app.add_typer(events.app, name="events")



if __name__ == "__main__":
    app()
