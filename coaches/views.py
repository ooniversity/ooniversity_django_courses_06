from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach

def detail(request, coach_id):
    assistant = Course.objects.filter(assistant=coach_id)
    coach = Coach.objects.get(id=coach_id)
    teacher = Course.objects.filter(coach=coach_id)
    return render(request,  "coaches/detail.html", {'assistant': assistant, 'coach': coach, 'teacher': teacher})
