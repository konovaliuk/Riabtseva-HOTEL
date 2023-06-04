import hashlib
def encode(password: str):
    return hashlib.md5(password.encode()).hexdigest()