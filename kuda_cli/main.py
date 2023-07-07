from typing import Annotated

import typer
from typer import Typer

from pykuda2 import Mode
from kuda_cli.accounts import account_app

from kuda_cli.billing_and_betting import billing_and_betting_app
from kuda_cli.card import card_app
from kuda_cli.savings import savings_app
from kuda_cli.transaction import transaction_app
from kuda_cli.utils import update_settings, reset_settings
from rich import print as rprint

app = Typer(
    name="Kuda",
    help="a command line utility to interact with Kuda's open API",
)
app.add_typer(account_app, name="account", help="Accounts")
app.add_typer(billing_and_betting_app, name="bb", help="Billing and betting")
app.add_typer(card_app, name="card", help="Cards")
app.add_typer(savings_app, name="savings", help="Savings")
app.add_typer(transaction_app, name="txn", help="Transactions")


@app.command()
def config(email: str, api_key: str, mode: Mode = Mode.DEVELOPMENT):
    """Set the configurations for your kuda cli.

    Args:
        email: The email address to your kuda integration.
        api_key: The API key for your kuda integration.
        mode: The mode to run the cli.
    """
    # TODO: validate email
    update_settings(option="email", value=email)
    update_settings(option="api_key", value=api_key)
    update_settings(option="mode", value=mode)
    rprint("Credentials saved! :boom:")


@app.command()
def config_interactive(
    email: Annotated[str, typer.Option(prompt=True)],
    api_key: Annotated[str, typer.Option(prompt="API Key")],
    mode: Annotated[Mode, typer.Option(prompt="Mode")] = Mode.DEVELOPMENT,
):
    """Set the configurations of you cli in interactive mode.
    """
    update_settings(option="email", value=email)
    update_settings(option="api_key", value=api_key)
    update_settings(option="mode", value=mode)
    rprint("credentials saved! :boom:")


@app.command()
def reset():
    """Reset your configurations.

    This deletes all existing configurations for your kuda cli.
    """
    reset_settings()
    rprint("credentials cleared! :boom:")

@app.command()
def version() -> str:
    rprint("Kuda CLI Version 0.1.0")


def run():
    """Entry point for the app"""
    app()


if __name__ == "__main__":
    run()
