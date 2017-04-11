from django.shortcuts import render
from courses.models import Course,Lessons
# Create your views here.

def list_courses(request):
    context = Course.objects.all()
    return  render(request,('index.html'),{'list_courses': context})

def details(request,**kwargs):
    id = request.GET.get(**kwargs)
    context = Lessons.get_list_lessons(id)
    return render(request,('courses.html'),{'deails':context})