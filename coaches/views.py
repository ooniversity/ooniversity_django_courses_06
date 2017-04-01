from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach

def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    teacher = Course.objects.filter(coach_id=coach_id)
    assistant = Course.objects.filter(assistant_id=coach_id)
    return render(request, "coaches/detail.html", {'coach': coach, 'teacher': teacher, 'assistant': assistant})

