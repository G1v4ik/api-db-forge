from django.db import models


active_choices = (
    (-1, 'Не состоит'),
    (0, 'рассматривается'),
    (1, 'действует')
)


class UserBase(models.Model):
    class Meta:
        abstract = True 

    telegram_id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    berth_day = models.DateField()
    is_active = models.IntegerField(choices=active_choices, default=active_choices[1])


class Groups(models.Model):
    id_group = models.AutoField(primary_key=True, unique=True)
    telegram_id_student = models.OneToOneField('Student', on_delete=models.PROTECT)
    id_grouptheory = models.ForeignKey('GroupTheory', on_delete=models.PROTECT)


class Driving(models.Model):
    id_driving = models.AutoField(primary_key=True, unique=True)
    telegram_id_student = models.ForeignKey('Student', unique=True, null=True, on_delete=models.PROTECT)
    telegram_id_teacher = models.ForeignKey('Teacher', null=True, on_delete=models.PROTECT)
    datetime_driving = models.DateTimeField()
    errors = models.IntegerField(default=-1)


class GroupTheory(models.Model):
    id_grouptheory = models.AutoField(primary_key=True, unique=True)
    telegram_id_teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, unique=True)
    name_group = models.CharField(max_length=30, unique=True)
    time_lesson = models.TimeField()
    theory_studied = models.BooleanField(default=False)
    date_exam_theory = models.DateTimeField()


class TimeWork(models.Model):
    id_timework = models.AutoField(primary_key=True, unique=True)
    work_begin = models.TimeField()
    work_end = models.TimeField()


class Student(UserBase):
    
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

