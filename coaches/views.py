from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course
from django.http import Http404


def detail(request, id):
    try:
        coach = Coach.objects.get(pk=int(id))
    except Coach.DoesNotExist:
        raise Http404("No coach or assistent id=" + id)

    return render(request, 'coaches/detail.html', {'coach' : coach})