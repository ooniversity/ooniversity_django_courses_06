import math

from django.shortcuts import render

MSG_NOT_DEFINED = 'коэффициент не определен'
MSG_NOT_INT = 'коэффициент не целое число'
MSG_A_IS_ZERO = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
MSG_ONE_SQUARE_ROOT = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s'
MSG_TWO_SQUARE_ROOTS = 'Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s'
MSG_D_LESS_THAN_ZERO = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

create_message = lambda key, msg: str(key) + "<br /><i>%s</i>" % msg


def quadratic_results(request):
    vars = {
        'a': request.GET.get('a', ''),
        'b': request.GET.get('b', ''),
        'c': request.GET.get('c', '')
    }
    errors = False
    for key in vars.keys():
        if vars[key] != "":
            try:
                vars[key] = int(vars[key])
                if key == 'a' and vars[key] == 0:
                    vars[key] = create_message(vars[key], MSG_A_IS_ZERO)
                    errors = True
            except ValueError:
                vars[key] = create_message(vars[key], MSG_NOT_INT)
                errors = True
        else:
            vars[key] = create_message(vars[key], MSG_NOT_DEFINED)
            errors = True
    if not errors:
        a = vars['a']
        b = vars['b']
        c = vars['c']
        message = str()
        d = b ** 2 - 4 * a * c
        vars['d'] = d
        if d >= 0:
            x1 = (-b + math.sqrt(d)) / 2 * a
            x2 = (-b - math.sqrt(d)) / 2 * a
            message = MSG_ONE_SQUARE_ROOT % x1 if d == 0 else \
                      MSG_TWO_SQUARE_ROOTS % (x1, x2)
        else:
            message = MSG_D_LESS_THAN_ZERO
        vars['message'] = message
    return render(request, 'results.html', vars)
