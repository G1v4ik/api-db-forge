# api driving school

## register new user

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

