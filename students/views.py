from django.shortcuts import render, redirect, reverse
from . models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages

# Create your views here.
def list_view(request):
    data = request.GET
    course = None
    if data:
        course_id = data['course_id']
        course = Course.objects.get(id=course_id)
        students_list = Student.objects.filter(courses__id=course_id)
    else:
        students_list = Student.objects.all()
    
    return render(request, 'students/list.html', {'students_list':students_list, 'current_course': course})

def detail(request, student_id):
    student = Student.objects.get(id=student_id)

    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Student {}{} has been successfully added.'.format(data['name'], data['surname']))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form':form})

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            data = form.cleaned_data
            
            student.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:detail', pk)
    else:
        form = StudentModelForm(instance=student)

    
    
    return render(request, "students/edit.html", {'form':form})

def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
                
            
            messages.success(request, 'Info on {} {} has been successfully deleted'.format(student.name, student.surname))
            student.delete()
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)

    
    
    return render(request, "students/remove.html", {'student':student})




