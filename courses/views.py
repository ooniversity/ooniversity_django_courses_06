from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, id):
#def detail(request, course_id_):
    #course_ = Course.objects.filter(pk = int(course_id_))
    #lessons = Lesson.objects.filter(course_id = int(course_id_))
    #return render(request, 'courses/detail.html', {'course_': course_[0], 'lessons': lessons})
    course = Course.objects.get(id=id)
    lesson = Lesson.objects.filter(course=id)
    context = {'course': course, 'lessons': lesson}
    return render(request, "courses/detail.html", context)

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course {0} has been successfully added.'.format(course.name))
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', id)
    form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course {0} has been deleted.'.format(course.name))
        return redirect('/')
    return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request, id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, 'Lesson {0} has been successfully added.'.format(lesson.subject))
            return redirect('courses:detail', id)
    else:
        form = LessonModelForm(initial={'course':id})
    return render(request, 'courses/add_lesson.html', {'form': form})


