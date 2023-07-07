from typing import Optional

from pykuda2 import TransferInstruction, TransactionStatus
from typer import Typer
from kuda_cli.utils import get_kuda_wrapper, strip_raw, override_output, colorized_print


transaction_app = Typer()


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_banks(request_reference: Optional[str] = None, data_only: bool = False):
    return get_kuda_wrapper().transactions.get_banks(request_reference=request_reference)


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def confirm_transfer_recipient(
    beneficiary_account_number: str,
    beneficiary_bank_code: str,
    sender_tracking_reference: Optional[str],
    is_request_from_virtual_account: bool,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.confirm_transfer_recipient(
        beneficiary_bank_code=beneficiary_bank_code,
        beneficiary_account_number=beneficiary_account_number,
        sender_tracking_reference=sender_tracking_reference,
        is_request_from_virtual_account=is_request_from_virtual_account,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def fund_transfer(
    beneficiary_account: str,
    beneficiary_bank_code: str,
    beneficiary_name: str,
    amount: int,
    narration: str,
    name_enquiry_session_id: str,
    sender_name: str,
    client_fee_charge: int = 0,
    client_account_number: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.fund_transfer(
        beneficiary_bank_code=beneficiary_bank_code,
        beneficiary_name=beneficiary_name,
        amount=amount,
        narration=narration,
        name_enquiry_session_id=name_enquiry_session_id,
        sender_name=sender_name,
        client_fee_charge=client_fee_charge,
        client_account_number=client_account_number,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def virtual_account_fund_transfer(
    tracking_reference: str,
    beneficiary_account: str,
    amount: int,
    beneficiary_name: str,
    narration: str,
    beneficiary_bank_code: str,
    sender_name: str,
    name_enquiry_id: str,
    client_fee_charge: int = 0,
    client_account_number: Optional[str] = None,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.virtual_account_fund_transfer(
        tracking_reference=tracking_reference,
        beneficiary_account=beneficiary_account,
        amount=amount,
        beneficiary_name=beneficiary_name,
        narration=narration,
        beneficiary_bank_code=beneficiary_bank_code,
        sender_name=sender_name,
        name_enquiry_id=name_enquiry_id,
        client_fee_charge=client_fee_charge,
        client_account_number=client_account_number,
        request_reference=request_reference,
    )


def process_transfers(
    fund_transfer_instructions: list[TransferInstruction],
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    # WARNING: Not exposed because typer can't accept class as input
    return get_kuda_wrapper().transactions.process_transfers(
        fund_transfer_instructions=fund_transfer_instructions,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_transfer_instructions(
    account_number: str,
    reference: str,
    amount: int,
    original_request_ref: str,
    status: TransactionStatus,
    page_number: int,
    page_size: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_transfer_instructions(
        account_number=account_number,
        reference=reference,
        amount=amount,
        original_request_ref=original_request_ref,
        status=status,
        page_number=page_number,
        page_size=page_size,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_transaction_logs(
    request_reference: str,
    response_reference: str,
    transaction_date: str,
    has_transaction_date_range_filter: bool,
    start_date: str,
    end_date: str,
    page_size: int,
    page_number: int,
    fetch_successful_records: bool = False,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_transaction_logs(
        request_reference=request_reference,
        response_reference=response_reference,
        transaction_date=transaction_date,
        has_transaction_date_range_filter=has_transaction_date_range_filter,
        start_date=start_date,
        end_date=end_date,
        page_size=page_size,
        page_number=page_number,
        fetch_successful_records=fetch_successful_records,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_transaction_history(
    page_size: int,
    page_number: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_transaction_history(
        page_size=page_size,
        page_number=page_number,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_filtered_transaction_history(
    page_size: int,
    page_number: int,
    start_date: str,
    end_date: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_filtered_transaction_history(
        page_size=page_size,
        page_number=page_number,
        start_date=start_date,
        end_date=end_date,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_virtual_account_transaction_history(
    tracking_reference: str,
    page_size: int,
    page_number: int,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_virtual_account_transaction_history(
        tracking_reference=tracking_reference,
        page_size=page_size,
        page_number=page_number,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_virtual_account_filtered_transaction_history(
    tracking_reference: str,
    page_size: int,
    page_number: int,
    start_date: str,
    end_date: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_virtual_account_filtered_transaction_history(
        tracking_reference=tracking_reference,
        page_size=page_size,
        page_number=page_number,
        start_date=start_date,
        end_date=end_date,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def get_status(
    is_third_party_bank_transfer: bool,
    transaction_request_reference: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.get_status(
        is_third_party_bank_transfer=is_third_party_bank_transfer,
        transaction_request_reference=transaction_request_reference,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def fund_virtual_account(
    tracking_reference: str,
    amount: int,
    narration: str,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.fund_virtual_account(
        tracking_reference=tracking_reference,
        amount=amount,
        narration=narration,
        request_reference=request_reference,
    )


@transaction_app.command()
@colorized_print
@override_output
@strip_raw
def withdraw_from_virtual_account(
    tracking_reference: str,
    amount: int,
    narration: str,
    client_fee_charge: int = 0,
    request_reference: Optional[str] = None,
    data_only: bool = False,
):
    return get_kuda_wrapper().transactions.withdraw_from_virtual_account(
        tracking_reference=tracking_reference,
        amount=amount,
        narration=narration,
        client_fee_charge=client_fee_charge,
        request_reference=request_reference,
    )
