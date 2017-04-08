from django.shortcuts import render
from quadratic.forms import QuadraticForm
from django.contrib import messages

def quadratic_results(request):
    if request.method == 'GET':
        form = QuadraticForm(request.GET)

    request_dictionary = {}
    for every in ['a', 'b', 'c']:
        request_dictionary[every] = request.GET.get(every, None)

    #isdigit
    if request_dictionary['a']:
        try:
            a = int(request_dictionary['a'])
            a_isdigit = True
            if a != 0:
                a_not_0 = True
            else:
                a_not_0 = False
                messages.error(request, form.clean_a(a))
        except:
            a_isdigit = False
            a_not_0 = None
    else:
        a_isdigit = None
        a_not_0 = None

    #
    if request_dictionary['b']:
        try:
            b = int(request_dictionary['b'])
            b_isdigit = True
        except:
            b_isdigit = False
    else:
        b_isdigit = None

    #
    if request_dictionary['c']:
        try:
            c = int(request_dictionary['c'])
            c_isdigit = True
        except:
            c_isdigit = False
    else:
        c_isdigit = None


    if a_isdigit and c_isdigit and b_isdigit and a != 0:
        D = b ** 2 - (4 * a * c)
        D_status = True
        request_dictionary['D'] = D
        request_dictionary['D_status'] = True

        if D > 0:
            x1 = (-b + D**0.5) / (2 * a)
            x2 = (-b - D**0.5) / (2 * a)
            request_dictionary['x1'] = x1
            request_dictionary['x2'] = x2
        elif D == 0:
            x1 = -b / (2 * a)
            request_dictionary['x1'] = x1

    request_dictionary['a_isdigit'] = a_isdigit
    request_dictionary['b_isdigit'] = b_isdigit
    request_dictionary['c_isdigit'] = c_isdigit
    request_dictionary['form'] = form

    context = request_dictionary

    return render(request, 'results.html', context)
