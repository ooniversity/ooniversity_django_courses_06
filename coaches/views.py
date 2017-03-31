from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.http import Http404


def detail(request, id):
    try:
        coach = Coach.objects.get(pk=int(id))
    except Coach.DoesNotExist:
        raise Http404("No coach or assistent id=" + id)

    return render(request, 'coach/detail.html', {
    				'coach': coach,
    				'teachercorses' : coach.coach_courses, 
    				'assistantcorses' : coach.assistant_courses})

def list_view(request):
	coachs = Coach.objects.all()
	return render(request, 'coach/list.html', {'coachs': coachs })