from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, coach_id):
    coach = Coach.objects.filter(id=int(coach_id)).first()
    course_couch = Course.objects.filter(coach = coach.id)
    course_assist = Course.objects.filter(assistant = coach.id)
    print(course_couch)
    return render(request, 'coaches/detail.html', {
				    'coach': coach,
				    'course_couch': course_couch,
				    'course_assist': course_assist,	
				    })
