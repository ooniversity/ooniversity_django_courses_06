from django.shortcuts import render
from math import sqrt
from django.http import QueryDict


def quadratic_results(request):
    def try_int(data):
        my_int = data
        if data == '':
            res = 'коэффициент не определен'
        else:
            try: 
                my_int = int(data)
                res = ''           
            except: 
                res = 'коэффициент не целое число'
        return res, my_int 
       
    url_data = request.GET
    a = url_data['a'] if url_data.__contains__('a') else ''
    b = url_data['b'] if url_data.__contains__('b') else ''
    c = url_data['c'] if url_data.__contains__('c') else ''
    res_a, a = try_int(a)                                       
    res_b, b = try_int(b)   
    res_c, c = try_int(c) 
    if a == 0:
        res_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        my_discr = ''
        res_qadr = ''
    elif a == '' or b == '' or c == '':
        my_discr = ''
        res_qadr = ''
    else:
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

    return render(request, 'results.html', {
            'a': a,
            'b': b,
            'c': c,
            'res_a': res_a,
            'res_b': res_b,
            'res_c': res_c,
            'discr': my_discr,
            'res_qadr': res_qadr
})
