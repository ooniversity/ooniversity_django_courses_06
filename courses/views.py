from django.shortcuts import render
from courses.models import Course,Lessons
# Create your views here.

def list_courses(request):
    context = Course.objects.all()
    return  render(request,('index.html'),{'list_courses': context})

def lessons_list(request,a):
    names_course = {1:'Python-Basics',2:'Python-Web Django',3:'JS Beginer'}
    id = Course.get_course_id_per_name_of_course(names_course[a])
    context = Lessons.get_list_lessons(id)
    return render(request,('courses.html'),{'lessons_list':context})