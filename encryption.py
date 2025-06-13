from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("AES_KEY", "").encode()

if len(KEY) not in [16, 24, 32]:
    raise ValueError(f"Invalid AES key length: {len(KEY)} bytes. It must be 16, 24, or 32 bytes.")

def encrypt_file(file_data):
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(file_data, AES.block_size))
    return iv + encrypted

def decrypt_file(encrypted_data):
    iv = encrypted_data[:16]
    if len(iv) != 16:
        raise ValueError(f"Incorrect IV length: {len(iv)} bytes (must be 16)")
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted
