from typing import Annotated

from pydantic import AfterValidator
from fastapi import HTTPException, status


def name_validator(name: str) -> str:
    name_parts = name.split()
    new_name = ""
    for name_part in name_parts:
        name_part.strip()
        if name_part.isspace():
            continue
        if not name_part.isalpha():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid name")
        if len(new_name) == 0:
            new_name += name_part.capitalize()
            continue
        new_name += " " + name_part.capitalize()
    total_letters = 0
    for letter in new_name:
        if letter.isalpha():
            total_letters += 1
            if total_letters == 3:
                break
    if total_letters < 3 or len(new_name) > 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid name size")
    return new_name


Name = Annotated[str, AfterValidator(name_validator)]