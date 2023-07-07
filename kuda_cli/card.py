from typing import Optional

from typer import Typer
from kuda_cli.utils import get_kuda_wrapper, strip_raw, override_output, colorized_print
from pykuda2.utils import Gender, CardChannel

card_app = Typer()


@card_app.command()
@colorized_print
@override_output
@strip_raw
def request_card(
    tracking_reference: str,
    name_on_card: str,
    country: str,
    gender: Gender,
    additional_phone_number: str,
    delivery_city: str,
    delivery_lga: str,
    delivery_landmark: str,
    date_of_birth: str,
    delivery_state: str,
    delivery_street_no_and_name: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.request_card(
        name_on_card=name_on_card,
        country=country,
        gender=gender,
        additional_phone_number=additional_phone_number,
        delivery_city=delivery_city,
        delivery_lga=delivery_lga,
        delivery_landmark=delivery_landmark,
        date_of_birth=date_of_birth,
        delivery_state=delivery_state,
        delivery_street_no_and_name=delivery_street_no_and_name,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def get_cards(
    tracking_reference: str,
    simulate_request: bool = False,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.get_cards(
        tracking_reference=tracking_reference,
        simulate_request=simulate_request,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def activate_card(
    pan: int,
    cvv: int,
    id: int,
    tracking_reference: str,
    simulate_request: bool = False,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.activate_card(
        pan=pan,
        cvv=cvv,
        id=id,
        tracking_reference=tracking_reference,
        simulate_request=simulate_request,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def deactivate_card(
    id: int,
    tracking_reference: str,
    simulate_request: bool = False,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.deactivate_card(
        id=id,
        tracking_reference=tracking_reference,
        simulate_request=simulate_request,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def set_card_limit(
    id: int,
    tracking_reference: str,
    channel: CardChannel,
    limit: int,
    simulate_request: bool = False,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.set_card_limit(
        id=id,
        tracking_reference=tracking_reference,
        channel=channel,
        limit=limit,
        simulate_request=simulate_request,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def manage_card_channel(
    id: int,
    tracking_reference: str,
    channel: CardChannel,
    limit: int,
    simulate_request: bool = False,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.manage_card_channel(
        id=id,
        tracking_reference=tracking_reference,
        channel=channel,
        limit=limit,
        simulate_request=simulate_request,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def change_card_pin(
    id: int,
    tracking_reference: str,
    new_pin: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.change_card_pin(
        id=id,
        tracking_reference=tracking_reference,
        new_pin=new_pin,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def block_card(
    tracking_reference: str,
    id: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.block_card(
        tracking_reference=tracking_reference,
        id=id,
        request_reference=request_reference,
    )


@card_app.command()
@colorized_print
@override_output
@strip_raw
def unblock_card(
    tracking_reference: str,
    id: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().cards.unblock_card(
        tracking_reference=tracking_reference,
        id=id,
        request_reference=request_reference,
    )
