import datetime
from typing import Any
from os import getenv

import jwt
from dotenv import load_dotenv


load_dotenv()
JWT_KEY = getenv("JWT_KEY")


def create_jwt(payload: dict[str, Any]) -> str:
    if not payload.get("exp"):
        payload["exp"] = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
    return jwt.encode(payload, JWT_KEY, "HS256")


def decode_jwt(token: str) -> dict[str, Any]:
    return jwt.decode(token, JWT_KEY, "HS256")
