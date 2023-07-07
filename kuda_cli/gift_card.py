from typing import Optional

from typer import Typer
from kuda_cli.utils import get_kuda_wrapper, strip_raw, override_output, colorized_print


gift_card_app = Typer()


@gift_card_app.command()
@colorized_print
@override_output
@strip_raw
def get_gift_cards(request_reference: Optional[str] = None, data_only: bool = False):
    return get_kuda_wrapper().gift_cards.get_gift_cards(request_reference=request_reference)


@gift_card_app.command()
@colorized_print
@override_output
@strip_raw
def purchase_gift_card(
    amount: int,
    customer_name: str,
    customer_mobile: str,
    customer_email: str,
    biller_identifier: str,
    note: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().gift_cards.purchase_gift_card(
        amount=amount,
        customer_name=customer_name,
        customer_mobile=customer_mobile,
        customer_email=customer_email,
        biller_identifier=biller_identifier,
        note=note,
        request_reference=request_reference,
    )


@gift_card_app.command()
@colorized_print
@override_output
@strip_raw
def purchase_gift_card_from_virtual_account(
    tracking_reference: str,
    amount: int,
    customer_name: str,
    customer_mobile: str,
    customer_email: str,
    biller_identifier: str,
    note: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().gift_cards.purchase_gift_card_from_virtual_account(
        tracking_reference=tracking_reference,
        amount=amount,
        customer_name=customer_name,
        customer_mobile=customer_mobile,
        customer_email=customer_email,
        biller_identifier=biller_identifier,
        note=note,
        request_reference=request_reference,
    )


@gift_card_app.command()
@colorized_print
@override_output
@strip_raw
def get_gift_card_status(
    tracking_reference: str,
    amount: int,
    customer_name: str,
    customer_mobile: str,
    customer_email: str,
    biller_identifier: str,
    note: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().gift_cards.get_gift_card_status(
        tracking_reference=tracking_reference,
        amount=amount,
        customer_name=customer_name,
        customer_mobile=customer_mobile,
        customer_email=customer_email,
        biller_identifier=biller_identifier,
        note=note,
        request_reference=request_reference,
    )
