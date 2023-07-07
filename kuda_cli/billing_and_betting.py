from typing import Optional
from pykuda2.utils import BillType
from typer import Typer
from kuda_cli.utils import get_kuda_wrapper, strip_raw, override_output, colorized_print

billing_and_betting_app = Typer()


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def get_bill_type_options(
    bill_type: BillType,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.get_bill_type_options(
        bill_type=bill_type, request_reference=request_reference
    )


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def verify_customer_before_purchase(
    tracking_reference: str,
    kuda_bill_item_identifier: str,
    customer_identification: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.verify_customer_before_purchase(
        tracking_reference=tracking_reference,
        kuda_bill_item_identifier=kuda_bill_item_identifier,
        customer_identification=customer_identification,
        request_reference=request_reference,
    )


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def purchase_bill(
    amount: int,
    bill_item_identifier: str,
    customer_identifier: str,
    phone_number: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.purchase_bill(
        amount=amount,
        bill_item_identifier=bill_item_identifier,
        customer_identifier=customer_identifier,
        phone_number=phone_number,
        request_reference=request_reference,
    )


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def purchase_bill_from_virtual_account(
    tracking_reference: str,
    amount: int,
    bill_item_identifier: str,
    phone_number: str,
    customer_identifier: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.purchase_bill_from_virtual_account(
        tracking_reference=tracking_reference,
        amount=amount,
        bill_item_identifier=bill_item_identifier,
        phone_number=phone_number,
        customer_identifier=customer_identifier,
        request_reference=request_reference,
    )


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def get_bill_purchase_status(
    bill_request_ref: Optional[str] = None,
    bill_response_reference: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.get_bill_purchase_status(
        bill_request_ref=bill_request_ref,
        bill_response_reference=bill_response_reference,
        request_reference=request_reference,
    )


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def get_purchased_bills(
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.get_purchased_bills(
        request_reference=request_reference
    )


@billing_and_betting_app.command()
@colorized_print
@override_output
@strip_raw
def get_purchased_bill_from_virtual_account(
    tracking_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().billing_and_betting.get_purchased_bill_from_virtual_account(
        tracking_reference=tracking_reference, request_reference=request_reference
    )
