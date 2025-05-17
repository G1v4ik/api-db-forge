import pyotp
import requests
import random


token = pyotp.TOTP('IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P').now()

data_newuser = {
    "user":{
        "telegram_id": random.randint(100_000, 999_999),
        "name": "ivan",
        "surname": "Ivanov",
        "phone": "89999999999",
        "email": "ivanov@gmail.com",
        "berth_day": "2000-02-11",
    }
}


json_new_student = {
    "user": {
        "telegram_id": random.randint(100_000, 999_999),
        "name": "teacher_name",
        "surname": "teacher_surname",
        "phone": random.randint(10000000000, 99999999999),
        "email": "email_teacher@gmail.com",
        "berth_day": "2000-10-22"}
}

json_new_teacher = {
    "user": {
        "telegram_id": random.randint(100_000, 999_999),
        "name": "teacher_name",
        "surname": "teacher_surname",
        "phone": random.randint(10000000000, 99999999999),
        "email": "email_teacher@gmail.com",
        "berth_day": "2000-10-22"
    }
}




base_url = 'http://127.0.0.1:8000/api/v1.1_beta/driving-school/'

academy_api_utl = 'http://127.0.0.1:8000/api/v1.1_beta/academy/'

class TestAPI:
    def __init__(self, url, json_data):
        self.url = url
        self.json = json_data
        self.result_request = ''
        self.requests = requests
        self.token = pyotp.TOTP('IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P').now()
        self.save_json = {}
        self.json_newuserbot = {
            "user": {
                "username": "Forge",
                "email": "forge@gmail.com",
                "password": "123456789",
                "token": "IZXXEZ3FL5ZWKY3SMV2GWZLZL54W633P"
            }
        }

    def new_user(self):
        new_userbot = self.requests.post(
            'http://127.0.0.1:8000/api/v1.1_beta/users/',
            json=self.json_newuserbot
        )
        self.results_save(new_userbot)


    def new_student(self):
        json_new_student = { 
            "user": {
                "telegram_id": random.randint(100_000, 999_999),
                "name": "teacher_name",
                "surname": "teacher_surname",
                "phone": random.randint(10000000000, 99999999999),
                "email": "email_teacher@gmail.com",
                "berth_day": "2000-10-22"
            }
        }

        return self.requests.post(
            f"{base_url}new/students/",
            json=json_new_student,
            headers=self.auth_headers
        )


    def new_teacher(self):
        json_new_teacher = {
            "user": {
                "telegram_id": random.randint(100_000, 999_999),
                "name": "teacher_name",
                "surname": "teacher_surname",
                "phone": random.randint(10000000000, 99999999999),
                "email": "email_teacher@gmail.com",
                "berth_day": "2000-10-22"
            }
        }

        return self.requests.post(
            f"{base_url}new/teachers/",
            json=json_new_teacher,
            headers=self.auth_headers
        )


    def new_test_data(self):
        self.new_student()
        self.new_teacher()


    def post(self):
        _post = self.requests.post(
            self.url, json=self.json,
            headers=self.auth_headers
        )
        self.results_save(_post)
    

    def get(self):
        _get = self.requests.get(
            self.url, json=self.json,
            headers=self.auth_headers
        )
        self.results_save(_get)
    

    def patch(self):
        _patch = self.requests.patch(
            self.url, json=self.json,
            headers=self.auth_headers
        )

        self.results_save(_patch)

    def results_save(self, method:requests.post.__class__ | requests.get.__class__):
        self.save_json = method.content
        self.result_request = f"status: {method.status_code}\ncontent: {self.get_json}"

    @property
    def auth_headers(self):
        auth_header = {
        "Authorization": f"Forge {str(self.token)}",
        }
        return auth_header

    @property
    def get_json(self):
        return self.save_json

    @property
    def results(self):
        return self.result_request


json_new_groups = {
   "groups": {
      "telegram_id_student": 903657,
      "id_grouptheory": 1
   }
}


json_new_grouptheory = {
    "user": {
        "telegram_id_teacher": 317656,
        "name_group": "new_group_theoru_is",
        "time_lesson": "15:30",
        "date_exam_theory": "2025-05-28"
    }
}


json_new_driving = {
    "driving": {
        "telegram_id_student": 296912,
        "telegram_id_teacher": 417284,
        "datetime_driving": "2025-05-10T15:00"
    }
}

json_new_timework = {
    "timework": {
        'id_timework': 1,
        "work_begin": "10:00",
    }
}

json_new_student_academy = {
    "data":{
        "telegram_id": random.randint(100_000, 999_999),
        "name": "student_name",
        "surname": "student_surname",
        "email": "student@gmail.com"
    }
}

json_new_courses_academy = {
    "data": {
        "title": "Курс, Python разработчик от нуля до профи"
    }
}

json_new_certificate_academy = {
    "data": {
        "id_student": 130071,
        "url": "http://blogshistory.ru",
        "id_courses": 1
    }
}

json_new_educationalmaterials_academy = {
    "data": {
        "id_courses": 2,
        "url": "http://blogshistory.ru",
    }
}

testapi = TestAPI(url=f'{academy_api_utl}educationalmaterials/', 
                  json_data=json_new_student_academy)

# testapi.new_user()
testapi.get()
# testapi.post()

# testapi.patch()

# for _ in range(10):
#     testapi.new_test_data()

print(testapi.results)
