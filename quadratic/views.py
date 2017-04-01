from django.shortcuts import render, redirect
from math import sqrt
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    context = {'error': False}
    if request.method == "GET":
        form = QuadraticForm()
    else:
        form = QuadraticForm(request.POST)
        if form.is_valid():
            a = form.clean_a()
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            my_discr = b*b - 4*a*c
            if my_discr < 0:
                res_qadr = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif my_discr == 0:
                x1 = -b /(2 * a)
                res_qadr = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x1)
            elif my_discr > 0:
                x1 = (-b + sqrt(my_discr)) / (2 * a)
                x2 = (-b - sqrt(my_discr)) / (2 * a)
                res_qadr = 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = '+ str(x2)

            if my_discr != '':
                my_discr = 'Дискриминант: ' + str(my_discr)

            context['a'] = a
            context['b'] = b
            context['c'] = c
            context['discr'] = my_discr
            context['res_qadr'] = res_qadr 

    context['form'] = form
    return render(request, 'quadratic/results.html', context)
