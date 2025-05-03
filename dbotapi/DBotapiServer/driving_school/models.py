from django.db import models


application_status_ru = {
    "consider": "рассматривается",
    "accept": "принят"
}


class UserBase(models.Model):
    class Meta:
        abstract = True 

    telegram_id = models.IntegerField()
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    berth_day = models.DateField()
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=30, choices=application_status_ru, default=application_status_ru['consider'])



class SchoolCar(models.Model):
    car_number = models.CharField(max_length=15)
    car_brand = models.CharField(max_length=20)
    car_color = models.CharField(max_length=20)
    description = models.TextField(name='desc')


class Driving(models.Model):
    fk_student = models.ForeignKey('Student', null=True, on_delete=models.PROTECT)
    fk_teacher = models.ForeignKey('Teacher', null=True, on_delete=models.PROTECT)
    fk_school_car = models.ForeignKey('SchoolCar', null=True, on_delete=models.PROTECT)
    fk_status_lesson = models.ForeignKey('StatusLesson', on_delete=models.PROTECT)
    datetime_driving = models.DateTimeField()
    errors = models.IntegerField()


class StatusLesson(models.Model):
    status_name = models.CharField(max_length=30)


class GroupTheory(models.Model):
    fk_teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)
    name_group = models.CharField(max_length=30)
    time_lesson = models.TimeField()
    theory_studied = models.BooleanField()
    date_exam_theory = models.DateTimeField()


class TimeWork(models.Model):
    time_day = models.TextChoices('am', 'pm')
    work_begin = models.TimeField()
    work_end = models.TimeField()


class Student(UserBase):
    fk_group_lesson = models.ForeignKey('GroupTheory', null=True, on_delete=models.SET_NULL)    

    
    @property
    def mode(self):
        return "student"


    def __str__(self):
        return f"student:{self.telegram_id} {self.name}"


class Teacher(UserBase):
    fk_time_work = models.ForeignKey('TimeWork', null=True, on_delete=models.SET_NULL)


    @property
    def mode(self):
        return "teacher"


    def __str__(self):
        return f"teacher:{self.telegram_id} {self.name}"


class Moderators(UserBase):
    
    @property
    def mode(self):
        return "moderator"

    def __str__(self):
        return f"moderator:{self.telegram_id} {self.name}"

