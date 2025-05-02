import pyotp
import requests

token = pyotp.TOTP('IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P').now()

data = {
    "user":{
        "email": "forge@gmail.com",
    }
}


print(requests.patch(
    'http://127.0.0.1:8000/api/v1.1_beta/', 
    json=data, 
    headers={
        "Authorization": f"Forge {str(token)}",
        }).content)