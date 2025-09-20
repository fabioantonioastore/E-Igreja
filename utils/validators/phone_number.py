from typing import Annotated

from pydantic import AfterValidator
import phonenumbers
from fastapi import HTTPException, status


def phone_number_validator(phone_number: str) -> str:
    parsed_phone_number = phonenumbers.parse(phone_number, "BR")
    if not phonenumbers.is_valid_number(parsed_phone_number):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid phone number")
    return phonenumbers.format_number(parsed_phone_number, phonenumbers.PhoneNumberFormat.E164)


PhoneNumber = Annotated[str, AfterValidator(phone_number_validator)]