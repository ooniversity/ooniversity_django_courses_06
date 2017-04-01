from django.shortcuts import render

import math

from quadratic.forms import QuadraticForm


def discriminant(data):

    a = data['a']
    b = data['b']
    c = data['c']

    dis_text_null = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    dis_text_result = 'Дискриминант: %(dis)d'

    result_text = 'Квадратное уравнение имеет два действительных корня: x1 = %(x1)s, x2 = %(x2)s'
    result_text_eq = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %(x1)s'

    dis = b ** 2 - 4 * a * c
    dis_result = dis_text_result % {'dis': dis}

    if dis >= 0:
        x1 = (-b + math.sqrt(dis)) / 2 * a
        x2 = (-b - math.sqrt(dis)) / 2 * a

        if dis == 0:
            result_text_x1_x2 = result_text_eq % {'x1': x1}
        else:
            result_text_x1_x2 = result_text % {'x1': x1, 'x2': x2}

    else:
        result_text_x1_x2 = dis_text_null

    context = {'dis_result': dis_result,
               'result_text_x1_x2': result_text_x1_x2,
               }

    return context


def quadratic_results(request):

    form = QuadraticForm()

    context = {}
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            dict_discriminant = discriminant(form.cleaned_data)
            context.update(dict_discriminant)

    context['form'] = form

    return render(request, 'quadratic/results.html', context)
