from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, Lesson

def index(request):
    courses = Course.objects.all()
    return render(request, "index.html", {"courses_list": courses})

def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')



