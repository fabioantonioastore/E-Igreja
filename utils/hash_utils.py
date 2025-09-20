import bcrypt


def hash_data(data: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_data = bcrypt.hashpw(data.encode("utf-8"), salt)
    return hashed_data


def check_data_and_hash(data: str, hashed_data: bytes) -> bool:
    return bcrypt.checkpw(data.encode("utf-8"), hashed_data)

