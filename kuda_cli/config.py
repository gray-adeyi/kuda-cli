from typer import Typer

config_app = Typer()

@config_app.command()
def config(email: str, api_key: str):
    ...

@config_app.command("config -i")
def config_interactive(email: str, api_key: str):
    ...

@config_app.command()
def reset():
    ...
