import hashlib


def hash_password(password: str) -> str:
    """Hash a password for storing."""
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()


def verify_password(stored_password: str, provided_password: str) -> bool:
    """Check if a provided password matches stored hash."""
    return stored_password == hash_password(provided_password)
