from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.get(id=int(coach_id))
    coach_courses = Course.objects.filter(coach = coach.id)
    assistant_courses = Course.objects.filter(assistant = coach.id)
    return render(request, 'coaches/detail.html', {
				    'coach': coach,
				    'coach_courses': coach_courses,
				    'assistant_courses': assistant_courses,	
				    })
