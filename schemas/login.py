from fastapi import HTTPException, status
from pydantic import EmailStr, model_validator

from . import BaseSchema
from utils.validators import Name, Password, CPF, PhoneNumber


class SignUp(BaseSchema):
    name: Name
    cpf: CPF | None = None
    email: EmailStr | None = None
    phone_number: PhoneNumber | None = None
    password: Password

    @model_validator(mode="after")
    def check_signup_data(self) -> None:
        if not (
            self.cpf or
            self.email or
            self.phone_number
        ):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You need to send at least a CPF or email or phone number")
