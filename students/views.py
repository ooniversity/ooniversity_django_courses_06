from django.shortcuts import render
from students.models import Student
from courses.models import Course

# Create your views here.

def student_info(student_id):
    neW_ = []
    stdnt = Student.objects.filter(id=student_id)

    for x in stdnt:
        crs = Course.objects.filter(student=student_id)

        stR_ = []
        for item in crs:
            id_ = Course.objects.filter(name=item.name)[0].id
            #id_ = 1
            stR_.append((item.name,id_))
    neW_.append((x, stR_))
    return neW_




def list_view(request):
    print('ITS STUDENT detail VIEWS')
    #print('request.GET:', request.GET)

    try:
        students_of_course = Student.objects.filter(courses__id=request.GET['course_id'])
    except:
        students_of_course = Student.objects.filter()

    new_ = []
    for every in students_of_course:
        print(every.id)
        crs = Course.objects.filter(student=every.id)

        str_ = []
        for item in crs:
            print('item_name:', item.name)
            id_ = Course.objects.filter(name=item.name)[0].id
            #id_ = 1
            str_.append((item.name,id_))
        new_.append((every, str_))

    print('QWERTY1:', new_)
    return render(request, 'students/list.html', {'students_of_course': new_ })


def detail(request, student_id):
    all_student_info = student_info(student_id)
    print('XXL1:', all_student_info)
    #print('XXL2:', all_student_info[0][0][0].name)
    return render(request, 'students/detail.html', {'all_student_info': all_student_info})