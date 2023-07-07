from typing import Optional
from pykuda2.utils import TransactionType
from typer import Typer
from kuda_cli.utils import get_kuda_wrapper, strip_raw, override_output, colorized_print


savings_app = Typer()


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def create_plain_savings_account(
    name: str,
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.create_plain_savings_account(
        name=name,
        tracking_reference=tracking_reference,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_plain_savings_account(
    tracking_reference: str,
    primary_account_number: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_plain_savings_account(
        tracking_reference=tracking_reference,
        primary_account_number=primary_account_number,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_plain_savings_accounts(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_plain_savings_accounts(
        tracking_reference=tracking_reference, request_reference=request_reference
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def credit_or_debit_plain_savings_account(
    amount: int,
    narration: str,
    transaction_type: TransactionType,
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.credit_or_debit_plain_savings_account(
        amount=amount,
        narration=narration,
        transaction_type=transaction_type,
        tracking_reference=tracking_reference,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_plain_savings_account_transactions(
    page_size: int,
    page_number: int,
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_plain_savings_account_transactions(
        page_size=page_size,
        page_number=page_number,
        tracking_reference=tracking_reference,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def create_open_flexible_savings_account(
    savings_tracking_reference: str,
    name: str,
    virtual_account_tracking_reference: str,
    amount: int,
    duration: str,
    frequency: str,
    start_now: bool,
    start_date: Optional[str],
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.create_open_flexible_savings_account(
        name=name,
        virtual_account_tracking_reference=virtual_account_tracking_reference,
        amount=amount,
        duration=duration,
        frequency=frequency,
        start_now=start_now,
        start_date=start_date,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def pre_create_open_flexible_savings_account(
    savings_tracking_reference: str,
    name: str,
    virtual_account_tracking_reference: str,
    amount: int,
    duration: str,
    frequency: str,
    start_now: bool,
    start_date: str,
    is_interest_earning: bool,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.pre_create_open_flexible_savings_account(
        savings_tracking_reference=savings_tracking_reference,
        name=name,
        virtual_account_tracking_reference=virtual_account_tracking_reference,
        amount=amount,
        duration=duration,
        frequency=frequency,
        start_now=start_now,
        start_date=start_date,
        is_interest_earning=is_interest_earning,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_open_flexible_savings_account(
    tracking_reference: str,
    primary_account_number: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_open_flexible_savings_account(
        tracking_reference=tracking_reference,
        primary_account_number=primary_account_number,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_open_flexible_savings_accounts(
    tracking_reference: str,
    primary_account_number: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_open_flexible_savings_accounts(
        tracking_reference=tracking_reference,
        primary_account_number=primary_account_number,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def withdrawal_from_flexible_savings_account(
    amount: int,
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.withdrawal_from_flexible_savings_account(
        amount=amount,
        tracking_reference=tracking_reference,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_flexible_savings_account_transactions(
    tracking_reference: str,
    page_size: int,
    page_number: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_flexible_savings_account_transactions(
        tracking_reference=tracking_reference,
        page_size=page_size,
        page_number=page_number,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def create_fixed_savings_account(
    savings_tracking_reference: str,
    name: str,
    virtual_account_tracking_reference: str,
    amount: int,
    duration: str,
    frequency: str,
    start_now: bool,
    start_date: str,
    is_interest_earning: bool,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.create_fixed_savings_account(
        savings_tracking_reference=savings_tracking_reference,
        name=name,
        virtual_account_tracking_reference=virtual_account_tracking_reference,
        amount=amount,
        duration=duration,
        frequency=frequency,
        start_now=start_now,
        start_date=start_date,
        is_interest_earning=is_interest_earning,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_fixed_savings_account(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_fixed_savings_account(
        tracking_reference=tracking_reference, request_reference=request_reference
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_fixed_savings_accounts(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_fixed_savings_accounts(
        tracking_reference=tracking_reference, request_reference=request_reference
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def close_fixed_savings_account(
    amount: int,
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.close_fixed_savings_account(
        amount=amount,
        tracking_reference=tracking_reference,
        request_reference=request_reference,
    )


@savings_app.command()
@colorized_print
@override_output
@strip_raw
def get_fixed_savings_account_transactions(
    tracking_reference: str,
    page_number: int,
    page_size: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().savings.get_fixed_savings_account_transactions(
        tracking_reference=tracking_reference,
        page_number=page_number,
        page_size=page_size,
        request_reference=request_reference,
    )
