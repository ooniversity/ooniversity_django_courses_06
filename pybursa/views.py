from django.shortcuts import render
from courses.models import Course
# Create your views here.


def index (request):
    list_of_courses=Course.objects.all()
    return render(request,'index.html', {'courses': list_of_courses})
  
def contact(request):
    return render(request,'contact.html')

def student_list (request):
    return render(request,'student_list.html')

def student_detail(request):
    return render(request,'student_detail.html')


