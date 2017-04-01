from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    context = {'error': False}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            context['a'] = a = form.clean_a()
            context['b'] = b = form.cleaned_data['b']
            context['c'] = c = form.cleaned_data['c']
            if a and b and c:
                context['discr'] = my_discr = b*b - 4*a*c
                if my_discr == 0:
                    context['x1'] = -b /(2 * a)
                elif my_discr > 0:
                    context['x1'] = (-b + sqrt(my_discr)) / (2 * a)
                    context['x2'] = (-b - sqrt(my_discr)) / (2 * a)
    else:
        form = QuadraticForm()

    context['form'] = form

    return render(request, 'quadratic/results.html', context)
