from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from courses.models import Course
from django.contrib import messages

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
    try:
        students_of_course = Student.objects.filter(courses__id=request.GET['course_id'])
    except:
        students_of_course = Student.objects.filter()

    new_ = []
    for every in students_of_course:
        crs = Course.objects.filter(student=every.id)

        str_ = []
        for item in crs:
            id_ = Course.objects.filter(name=item.name)[0].id
            str_.append((item.name,id_))
        new_.append((every, str_))

    return render(request, 'students/list.html', {'students_of_course': new_ })

#def detail(request, student_id):
def detail(request, id):
    student_id = id
    all_student_info = student_info(student_id)
    return render(request, 'students/detail.html', {'all_student_info': all_student_info})

def create(request):
    if request.method == 'POST':
        print('Its  CREATE_POST_method!')
        form = StudentModelForm(request.POST)
        print("FORM_IS_VALID:", form.is_valid())
        if form.is_valid():
            print('Form is VALID!')
            student = form.save()
            messages.success(request,
                             'Student {0} {1} has been successfully added.'.format(student.name, student.surname))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, id):
    print('EDIT_method_id:', id)
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:list_view')
    form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on {0} {1} has been successfully deleted.'.format(student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
