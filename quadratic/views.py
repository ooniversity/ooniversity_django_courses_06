from django.shortcuts import render


def validation(value, first_value=False):
    value_error = ''
    not_int_error = 'коэффициент не целое число'
    none_error = 'коэффициент не определен'
    first_value_zero_error = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
    try:
        if len(value) == 0:
            value_error = none_error
        elif int(value) == 0 and first_value is True:
            value_error = first_value_zero_error
    except ValueError:
        value_error = not_int_error
    return(value_error)

def calc_root(order = 1):
    if order == 1:
        x = (-int(b) + int(d) ** (1 / 2)) / 2 * int(a)
    else:
        x = (-int(b) - int(d) ** (1 / 2)) / 2 * int(a)
    return x

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    error_a = validation(request.GET['a'], True)
    error_b = validation(request.GET['b'])
    error_c = validation(request.GET['c'])
    flag = False
    diskr = None
    messages = ''
    x1 = ''
    x2 = ''
    if error_a == '' and error_b == '' and error_c == '':
        flag = True
        diskr = int(b) ** 2 - 4 * int(a) * int(c)
        if diskr < 0:
            messages = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif diskr == 0:
            x1 = x2 = (-int(b) + int(diskr) ** (1 / 2)) / 2 * int(a)
            messages = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" %x1
        elif diskr > 0:
            x1 = (-int(b) + int(diskr) ** (1 / 2)) / 2 * int(a)
            x2 = (-int(b) - int(diskr) ** (1 / 2)) / 2 * int(a)
            messages = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1, x2)     

    context = {'a': a, 'b': b, 'c': c, 'error_a': error_a, 'error_b': error_b, 'error_c': error_c, 'diskr': diskr, 'flag' : flag, 'messages': messages}
    return render(request, 'quadratic/results.html', context)


