from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages

# Create your views here.
def detail (request,id):
    person=Student.objects.filter(pk=id).first()
    return render(request,'students/detail.html',{'person':person})

def list_view (request):
    pk = request.GET.get('course_id')
    if not pk:
        student = Student.objects.all()    
    else:
        student = Student.objects.filter(courses__id=pk)    
    courses_list = Course.objects.all()
    return render(request,'students/list.html',{'cid':pk, 'stud_on_course':student,'courses_list':courses_list})

def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Student {} {} has been successfully added.".format(student.name, student.surname))
            return redirect('/students/')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Info on the student has been successfully changed.")
            return redirect('/students/')
        else:
            form = StudentModelForm(request.POST, instance=student)
    form = StudentModelForm(instance=student)
    print(form['surname'].value(),'\n',form)
    return render(request, 'students/edit.html', {'form': form})

def remove(request, id):
        student = Student.objects.get(pk=id)
        if request.method == "POST":
            student.delete()
            messages.success(request, "Info on {} {} has been successfully deleted.".format(student.name, student.surname))
            return redirect('/students/')
        return render(request, 'students/remove.html', {'student': student})
