from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encode_to_hash_pwd(password: str) -> str:
    return pwd_context.hash(password)


def verify_hash_pwd(req_pwd: str, db_pwd: str) -> bool:
    return pwd_context.verify(req_pwd, db_pwd)
