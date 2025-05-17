# Academy API

## required for post and get requests

- Header must contain

```json
{
    "Authorization": "{UserName} {TOKEN:length 6}"
}
```

## New student/teacher

__URL:__ <http://example.com/students> (POST)

```json
{
    "data":{
        "telegram_id": telegram_id: integer,
        "name": "student_name",
        "surname": "student_surname",
        "email": "student@gmail.com"
    }
}
```

## New courses

__URL:__ <http://example.com/courses> (POST)

```json
{
    "data": {
        "title": "Курс, Python разработчик от нуля до профи"
    }
}
```

## New certificate_academy

__URL:__ <http://example.com/certificates> (POST)

```json
{
    "data": {
        "id_student": 11111 (student telegram_id),
        "url": "http://blogshistory.ru",
        "id_courses": 1
    }
}
```

## New educational materials

__URL:__ <http://example.com/educationalmaterials> (POST)

```json
{
     "data": {
        "id_courses": 1,
        "url": "http://blogshistory.ru",
    }
}
```

## Get info (students / courses / certificates / educationalmaterials) as {X}

__URL: <http://example.com/{X}> and <http://example.com/{X}/{id}>__

__student (to get information about all {X}, use the first link):__

```json
{
    "result": 
    [
        {
            "telegram_id": 130071, 
            "name": "student_name", 
            "surname": "student_surname", 
            "email": "student@gmail.com"}, 
        {
            "telegram_id": 599193, 
            "name": "student_name", 
            "surname": "student_surname", 
            "email": "student@gmail.com"}, 
        {
            "telegram_id": 713260, 
            "name": "student_name", 
            "surname": "student_surname", 
            "email": "student@gmail.com"}, 
        {
            "telegram_id": 787000, 
            "name": "student_name", 
            "surname": "student_surname", 
            "email": "student@gmail.com"},
        {
            "telegram_id": 979555, 
            "name": "student_name", 
            "surname": "student_surname", 
            "email": "student@gmail.com"}
    ]
}
```

__courses__

> if u use Russ words then use json.load for decode this

```json
{
    "result": [
        {
            "pk": 1, 
            "title": "\\u041a\\u0443\\u0440\\u0441, Python ..."
        }
    ]
}

```

__certificates__

```json
{
    "result": [
        {
            "pk": 1, 
            "url": "http://blogshistory.ru", 
            "id_student": 130071, 
            "id_courses": 1
        }
    ]
}
```

__educationalmaterials__

```json
{
   "result": 
    [
        {
            "pk": 1, 
            "url": "http://blogshistory.ru", 
            "id_courses": 1
        }, 

        {
            "pk": 2, 
            "url": "http://blogshistory.ru", 
            "id_courses": 1
        }, 
    ]
}
```
