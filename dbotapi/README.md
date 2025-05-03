# api driving school

## register new user for telegram bot

post: url: @/v1.1_beta/users/

- @ - domen (https://domen.com)

```json
{
    "user": {
        "username": "Forge",
        "email": "forge@gmail.com",
        "password": "123456789",
        "token": "IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P"
    }

}

```

### О password и token
 
- password: 128 < password > 8
- token: токен типа base32, который вы генерируете сами


## register new student

post: @/api/v1.1_beta/driving-school/new/students/

```python
import pyotp
import requests

token = pyotp.TOTP('IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P').now()

data = {
    "user":{
        "telegram_id": 12341234,
        "name": "ivan",
        "surname": "Ivanov",
        "phone": "89999999999",
        "email": "ivanov@gmail.com",
        "berth_day": "2000-02-11",
        "mode": "student"
    }
}


print(requests.post(
    'http://127.0.0.1:8000/api/v1.1_beta/driving-school/new/students/', 
    json=data, 
    headers={
        "Authorization": f"Forge {str(token)}",
        }).content)

#output: b'{"user": {"telegram_id": 12341234, "name": "ivan", "surname": "Ivanov", "phone": "89999999999", "email": "ivanov@gmail.com", "berth_day": "2000-02-11", "mode": "student"}}'

```