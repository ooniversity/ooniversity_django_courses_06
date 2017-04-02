from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from students.forms import StudentModelForm 


def list_view(request):
    req = request.GET
    course_id = req.get('course_id', '')
    if course_id != '':
        course_students = Student.objects.filter(courses__id=course_id)
    else:
        course_students = Student.objects.all()
    return render(request, 'students/list.html', {
                           'students': course_students,	
                           })

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {
                           'student': student,	
                           })

def create(request):
    context = {'error': False}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            context['form'] = instance
            message = messages.success(request, "Student %s %s has been successfully added." %(instance.name, instance.surname))
            return redirect('/students/', messages=message)
    else:
        form = StudentModelForm()
    context['form'] = form
    return render(request, 'students/add.html', context)

def edit(request, student_id):
    context = {'error': False}
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            instance = form.save()
            context['form'] = instance
            messages.success(request, "Info on the student has been successfully changed." )
            return redirect('students:edit', student_id=student_id)
    else:
        form = StudentModelForm(instance=student)
    context['form'] = form
    return render(request, 'students/edit.html', context)

def remove(request, student_id):
    context = {'error': False}
    instance = Student.objects.get(id=student_id)
    if request.method == 'POST':
        message = messages.success(request, "Info on %s %s has been successfully deleted." %(instance.name, instance.surname))
        instance.delete()
        return redirect('/students/', message)
    else:
        form = StudentModelForm(instance)
    context['student'] = instance
    context['form'] = form
    return render(request, 'students/remove.html', context)
