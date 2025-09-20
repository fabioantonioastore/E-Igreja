from typing import Annotated
import re

from pydantic import AfterValidator
from fastapi import HTTPException, status


def password_validator(password: str) -> str:
    if len(password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must have at least 8 characters")
    if len(password) > 32:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The password is so big")
    if not re.search(r'[!@#$%^&*()_+-=? ]', password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must have at least 1 special character")
    if not re.search(r'[0-9]', password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must have at least 1 number")
    if not re.search(r'[A-Z]', password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must have at least 1 upper case letter")
    if not re.search(r'[a-z]', password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You must have at least 1 lower letter")
    return password


Password = Annotated[str, AfterValidator(password_validator)]