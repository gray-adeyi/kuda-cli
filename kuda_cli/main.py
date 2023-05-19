from typer import Typer
from kuda_cli.config import config_app

app = Typer()
app.add_typer(config_app, name="config")

def run():
    """Entry point for the app"""
    app()

if __name__ == "__main__":
    run()
