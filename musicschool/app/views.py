from django.shortcuts import render, redirect
from .models import Student
from.forms import *


# Create your views here.

def show_all_students(request):
    students = Student.objects.all()

    return render(request, 'students.html', {'students': students})


def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.surname = request.POST.get('surname')
        student.age = request.POST.get('age')
        student.speciality = request.POST.get('speciality')
        student.teacher_name = request.POST.get('teacher_name')
        student.teacher_surname = request.POST.get('teacher_surname')
        student.grade = request.POST.get('grade')
        student.save()
        return redirect('/')

    return render(request, 'edit_student.html', {'student': student})


def create_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentCreationForm()

    return render(request, 'create_student.html', {'form': form})
