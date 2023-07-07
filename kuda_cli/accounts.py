from typing import Optional

from typer import Typer
from kuda_cli.utils import get_kuda_wrapper, strip_raw, override_output, colorized_print

account_app = Typer()


@account_app.command()
@colorized_print
@override_output
@strip_raw
def create_virtual_account(
    email: str,
    phone_number: str,
    last_name: str,
    first_name: str,
    middle_name: str,
    business_name: str,
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.create_virtual_account(
        email=email,
        phone_number=phone_number,
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        business_name=business_name,
        tracking_reference=tracking_reference,
        request_reference=request_reference,
    )


@account_app.command()
@colorized_print
@override_output
@strip_raw
def update_virtual_account(
    self,
    tracking_reference: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.update_virtual_account(
        tracking_reference=tracking_reference,
        first_name=first_name,
        last_name=last_name,
        email=email,
        request_reference=request_reference,
    )


@account_app.command()
@colorized_print
@override_output
@strip_raw
def get_virtual_accounts(
    page_size: Optional[int] = 1,
    page_number: Optional[int] = 1,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.get_virtual_accounts(page_size, page_number, request_reference)


@account_app.command()
@colorized_print
@override_output
@strip_raw
def get_virtual_account(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.get_virtual_account(tracking_reference, request_reference)


@account_app.command()
@colorized_print
@override_output
@strip_raw
def disable_virtual_account(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.disable_virtual_account(
        tracking_reference=tracking_reference, request_reference=request_reference
    )


@account_app.command()
@colorized_print
@override_output
@strip_raw
def enable_virtual_account(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.enable_virtual_account(tracking_reference, request_reference)


@account_app.command()
@colorized_print
@override_output
@strip_raw
def get_admin_account_balance(
    request_reference: Optional[str] = None, data_only: bool = False
):
    return get_kuda_wrapper().accounts.get_admin_account_balance(request_reference)


@account_app.command()
@colorized_print
@override_output
@strip_raw
def get_virtual_account_balance(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().accounts.get_virtual_account_balance(
        tracking_reference=tracking_reference, request_reference=request_reference
    )
