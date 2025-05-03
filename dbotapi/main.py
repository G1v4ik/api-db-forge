import pyotp
import requests

token = pyotp.TOTP('IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P').now()

data = {
    "user":{
        "telegram_id": 12341234,
        "name": "Ivan",
        "surname": "Ivanov",
        "phone": "11111111111",
        "email": "ivan@gmail.com",
        "berth_day": "2000-03-21",
        "mode": "student"
    }
}


print(requests.post(
    'http://127.0.0.1:8000/api/v1.1_beta/driving-school/new/students/', 
    json=data, 
    headers={
        "Authorization": f"Forge {str(token)}",
        }).content)