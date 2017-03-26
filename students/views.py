from django.shortcuts import render
from courses.models import Course
from students.models import Student

# Create your views here.
def detail (request,sid):
    print(sid)
    return render(request,'students/detail.html')#,{'cid':cid})

def list_view (request):
    cid = request.GET.get('course_id')
    if not cid:
        return render(request,'student_list.html') # LIST OF ALL students and exit
    stud_on_course = Student.objects.filter(courses__id=cid)    
    print("STUD------",stud_on_course)
    courses_list = Course.objects.all()
    #courses_list={}
    #for each_student in stud_on_course:
        #courses_list[each_student.id]=[]
        #for each_course in Course.objects.filter(student__id=each_student.id):
            #courses_list[each_student.id].append(each_course.name)
    #print(courses_list)
        
    return render(request,'students/list.html',{'cid':cid, 'stud_on_course':stud_on_course,'courses_list':courses_list})