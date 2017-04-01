from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from students.forms import StudentModelForm
from students.models import Student


def list_view(request):
    if len(request.GET) == 0:
        student_list = Student.objects.all()
    else:
        course_id = request.GET['course_id']
        student_list = Student.objects.filter(courses__id=course_id)

    context = {'students': student_list}
    return render(request, 'students/list.html', context)


def detail(request, student_id):
    current_student = Student.objects.get(id=student_id)
    context = {'student': current_student}
    return render(request, 'students/detail.html', context)


def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            result_string = "Student %(name)s %(surname)s has been successfully added." % {'name': instance.name,
                                                                                           'surname': instance.surname}

            messages.success(request, result_string)
            return redirect('/students/')
    else:
        form = StudentModelForm()

    return render(request, 'students/add.html', {'form': form})


def edit(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            instance = form.save()
            result_string = "Info on the student has been successfully changed."
            messages.success(request, result_string)
            url_string = reverse('students:edit', args=(student_id,))
            return redirect(url_string)

    form = StudentModelForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})


def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    name = student.name
    surname = student.surname
    if request.method == "POST":
        student.delete()
        result_string = "Info on %(name)s %(surname)s has been successfully deleted." % {'name': name,
                                                                                         'surname': surname}
        messages.success(request, result_string)
        return redirect('/students/')

    delete_student = "Студент %(name)s %(surname)s будет удален" % {'name': name,
                                                                    'surname': surname}

    return render(request, 'students/remove.html', {'delete_student': delete_student})
