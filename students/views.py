from django.shortcuts import render
from students.models import Student
from courses.models import Course


# Create your views here.
def detail (request,sid):
    person=Student.objects.filter(id=sid).first()
    return render(request,'students/detail.html',{'person':person})

def list_view (request):
    cid = request.GET.get('course_id')
    if not cid:
        stud_on_course = Student.objects.all()    
    else:
        stud_on_course = Student.objects.filter(courses__id=cid)    
    courses_list = Course.objects.all()
       
    return render(request,'students/list.html',{'cid':cid, 'stud_on_course':stud_on_course,'courses_list':courses_list})