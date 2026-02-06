from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_data(data: str):
    return cipher.encrypt(data.encode())

def decrypt_data(token: bytes):
    return cipher.decrypt(token).decode()