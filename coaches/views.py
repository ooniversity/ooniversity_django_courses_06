from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course

# Create your views here.

def detail(request, coach_id):

    current_coach = Coach.objects.get(id=coach_id)
    courses_coach = Course.objects.filter(coach=current_coach)
    courses_assistant = Course.objects.filter(assistant=current_coach)

    context = {'coach': current_coach,
               'courses_coach': courses_coach,
               'courses_assistant': courses_assistant,
               }

    return render(request, 'coaches/detail.html', context)
