from typing import Annotated

from pydantic import AfterValidator
from fastapi import HTTPException, status
from validate_docbr import CPF as CPFValidator


def cpf_validator(cpf: str) -> str:
    if not CPFValidator().validate(cpf):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid CPF")
    if not cpf.isnumeric():
        new_cpf = ""
        for character in cpf:
            if character.isnumeric():
                new_cpf += character
        return new_cpf
    return cpf


CPF = Annotated[str, AfterValidator(cpf_validator)]