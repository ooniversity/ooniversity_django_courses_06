from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course


def index(request):
     courses = Course.objects.all()
     context = {'courses': courses}
     return render(request, "index.html", context)

def contact(request):
     return render(request, "contact.html")

def student_list(request):
     return render(request, "student_list.html")

def student_detail(request):
     return render(request, "student_detail.html")

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

