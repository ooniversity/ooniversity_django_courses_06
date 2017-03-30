from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach
from django.http import Http404

# Create your views here.


'''def detail(request, id):
    coach = Coach.objects.get(pk=id)
    coach_courses = Course.objects.filter(coach__id=id)
    assistant_courses = Course.objects.filter(assistant__id=id)

    context = {'coach': coach,
               'coach_courses': coach_courses,
               'assistant_courses': assistant_courses, }
    return render(request, 'coaches/detail.html', context)
'''


def detail(request, id):
    try:
        coach = Coach.objects.get(pk=id)
        # coach_courses = Course.objects.filter(coach__id=id)
        # assistant_courses = Course.objects.filter(assistant__id=id)
    except Coach.DoesNotExist:
        raise Http404("No coach or assistent id=" + id)

    context = {'coach': coach,
               'coach_courses': coach.coach_courses,
               'assistant_courses': coach.assistant_courses, }
    return render(request, 'coaches/detail.html', context)
