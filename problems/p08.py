import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

AES_KEY = b"Pay!Module#2024!"
BLOCK = AES.block_size


def encrypt_card(card_number: str) -> str:
    iv = os.urandom(BLOCK)
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    data = cipher.encrypt(pad(card_number.encode(), BLOCK))
    return base64.b64encode(iv + data).decode()


def decrypt_card(token: str) -> str:
    raw = base64.b64decode(token)
    cipher = AES.new(AES_KEY, AES.MODE_CBC, raw[:BLOCK])
    return unpad(cipher.decrypt(raw[BLOCK:]), BLOCK).decode()
