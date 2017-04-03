from django.shortcuts import render, redirect, reverse
from . models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm

# Create your views here.

def detail(request, course_id):
    
    course = Course.objects.get(id=course_id)
    lessons_list = Lesson.objects.filter(course=course)
    coach = Coach.objects.get(id=course.coach.id)
    assistant = Coach.objects.get(id=course.assistant.id)

    return render(request, "courses/detail.html", {'course':course, 'lessons_list': lessons_list, 'coach':coach, 'assistant':assistant})


def add(request):
    
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            form.save()
            return redirect('/')
    else:
        form = CourseModelForm()
        
    return render(request, "courses/add.html", {'form':form})


def edit(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            data = form.cleaned_data
            
            course.save()
            return reverse('edit', args=(pk,))
    else:
        form = CourseModelForm(instance=course)

    
    
    return render(request, "courses/edit.html", {'form':form})
    


#def add_lesson(request, request_id):


    
