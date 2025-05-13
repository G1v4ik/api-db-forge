from django.db import models

class AbstractBaseModel(models.Model):
    class Meta:
        abstract = True

    def get_pk(self):
        return self.pk

class Student(models.Model):
    telegram_id = models.IntegerField(
        primary_key=True,
        unique=True
    )
    name = models.CharField(
        max_length=15
    )
    surname = models.CharField(
        max_length=25
    )
    email = models.EmailField()


class Certificate(AbstractBaseModel):
    id_certificate = models.AutoField(
        primary_key=True, 
        unique=True
    )
    id_student = models.ForeignKey(
        "Student", on_delete=models.PROTECT
    )
    url = models.URLField()
    id_courses = models.ForeignKey(
        "Courses", on_delete=models.PROTECT
    )

class Courses(AbstractBaseModel):
    id_courses = models.AutoField(
        primary_key=True,
        unique=True
    )
    title = models.TextField()
    

class EducationalMaterials(AbstractBaseModel):
    id_ed_materials = models.AutoField(
        primary_key=True,
        unique=True,
        serialize=True
    )
    id_courses = models.ForeignKey(
        "Courses",
        on_delete=models.PROTECT
    )
    url = models.URLField()
