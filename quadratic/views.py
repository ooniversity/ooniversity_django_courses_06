from django.shortcuts import render
from django.http import HttpResponse

import math

def quadratic_results(request):
    # print('request: ', request.GET['c'] == '')
    # return HttpResponse(request.GET)

    data = request.GET

    if not data:
        return render(request, 'results.html')

    is_valid_factors = True

    error_messages = {
        'not_defined': 'коэффициент не определен',
        'not_integer': 'коэффициент не целое число',
        'is_zero': 'коэффициент при первом слагаемом уравнения не может быть равным нулю',
    }

    result_messages = {
        'discriminant_text': 'Дискриминант:',
        'two_roots': 'Квадратное уравнение имеет два действительных корня:',
        'no_roots': 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.',
        'one_root': 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:',
    }

    context = {
        'factors': [],
        'results': {},
    }

    a = data['a']
    b = data['b']
    c = data['c']

    a_item = {
        'item_name': 'a',
        'item_value': a
    }

    b_item = {
        'item_name': 'b',
        'item_value': b
    }

    c_item = {
        'item_name': 'c',
        'item_value': c
    }

    if a == '':
        a_item['error_message'] = error_messages['not_defined']
        is_valid_factors = False
    else:
        try:
            if int(a) == 0:
                a_item['error_message'] = error_messages['is_zero']
                is_valid_factors = False
        except ValueError:
            a_item['error_message'] = error_messages['not_integer']
            is_valid_factors = False

    if b == '':
        b_item['error_message'] = error_messages['not_defined']
        is_valid_factors = False
    else:
        try:
            int(b)
        except ValueError:
            b_item['error_message'] = error_messages['not_integer']
            is_valid_factors = False

    if c == '':
        c_item['error_message'] = error_messages['not_defined']
        is_valid_factors = False
    else:
        try:
            int(c)
        except ValueError:
            c_item['error_message'] = error_messages['not_integer']
            is_valid_factors = False

    context['factors'].append(a_item)
    context['factors'].append(b_item)
    context['factors'].append(c_item)

    if is_valid_factors:
        results = dict()

        A = int(a)
        B = int(b)
        C = int(c)

        D = B**2 - 4*A*C

        results['discriminant_text'] = result_messages['discriminant_text']
        results['discriminant'] = D

        if D < 0:
            results['root_text'] = result_messages['no_roots']
        elif D == 0:
            results['root_text'] = result_messages['one_root']
            results['x1'] = -B/(2*A)
        else:
            results['root_text'] = result_messages['two_roots']
            results['x1'] = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
            results['x2'] = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)

        context['results'] = results

    return render(request, 'results.html', context)
