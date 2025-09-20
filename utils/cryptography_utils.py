from os import getenv

from dotenv import load_dotenv
from cryptography.fernet import Fernet


load_dotenv()
CRYPTOGRAPHY_KEY = getenv("CRYPTOGRAPHY_KEY")


def encrypt(data: str) -> bytes:
    fernet = Fernet(CRYPTOGRAPHY_KEY)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data


def decrypt(encrypted_data: bytes) -> str:
    fernet = Fernet(CRYPTOGRAPHY_KEY)
    data = fernet.decrypt(encrypted_data).decode()
    return data
