from django import forms
from .models import *


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'speciality', 'teacher_name', 'teacher_surname', 'grade']
