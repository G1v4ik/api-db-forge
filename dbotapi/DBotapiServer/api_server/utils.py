import base64
import pyotp

from cryptography.fernet import Fernet

from django.conf import settings


def get_s_token():
    with open (f'{settings.BASE_DIR}{settings.STATIC_URL}token.key', 'r') as secrettoken:
        return secrettoken.read().encode('utf-8')


def is_base32(s):
    try:
        decode = base64.b32decode(s)

        encoded = base64.b32encode(decode).decode('utf-8')

        return encoded == s
    
    except Exception:
        return False



class MyToken:

    def __init__(self):
        self.fern = Fernet(get_s_token())


    def encrypt(self, data:str):
        return self.fern.encrypt(data.encode('utf-8'))
    
    
    def decrypt(self, data:bytes):
        return self.fern.decrypt(data)
