from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    speciality = models.CharField(max_length=255)
    teacher_name = models.CharField(max_length=50)
    teacher_surname = models.CharField(max_length=50)
    grade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} " \
               f"{self.speciality} {self.teacher_name}" \
               f" {self.teacher_surname} {self.grade}"

