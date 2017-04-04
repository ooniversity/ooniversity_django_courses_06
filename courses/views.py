from django.shortcuts import render, redirect
from django.urls import reverse
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson
from django.contrib import messages

# Create your views here.

def detail(request, course_id):
    current_course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=current_course).order_by('order')

    context = {'course': current_course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            result_string = "Course %(name)s has been successfully added." % {'name': instance.name}

            messages.success(request, result_string)
            return redirect('/')
    else:
        form = CourseModelForm()

    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):

    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            instance = form.save()
            result_string = "The changes have been saved."
            messages.success(request, result_string)
            url_string = reverse('courses:edit', args=(course_id,))
            return redirect(url_string)

    form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    name = course.name
    if request.method == "POST":
        course.delete()
        result_string = "Course %(name)s has been deleted." % {'name': name}

        messages.success(request, result_string)
        return redirect('/')

    delete_course = "Курс %(name)s будет удален" % {'name': name}

    return render(request, 'courses/remove.html', {'delete_course': delete_course})


def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            result_string = "Lesson %(subject)s has been successfully added." % {'subject': instance.subject}

            messages.success(request, result_string)
            url_string = reverse('courses:detail', args=(course_id,))
            return redirect(url_string)
    else:
        form = LessonModelForm(initial={'course': course})

    return render(request, 'courses/add_lesson.html', {'form': form})
