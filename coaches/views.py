from django.shortcuts import render
from courses.models import Course
from coaches.models import Coach

# Create your views here.
def detail (request, coaid):
    coach = Coach.objects.get(id=coaid)
    coach_on_courses = Course.objects.filter(coach__id=coaid)
    assistant_on_courses = Course.objects.filter(assistant__id=coaid)

    in_template = {'coach': coach,
               'coach_courses': coach_on_courses,
               'assistant_courses': assistant_on_courses,}
    return render(request, 'coaches/detail.html', in_template)