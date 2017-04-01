from django.shortcuts import render, redirect
from django.http import QueryDict
from math import sqrt
from quadratic.forms import QuadraticForm

def discriminant(a, b, c):
    return b * b - (4 * a * c)


def roots(discriminant, a, b) -> list:
    '''Return root(s) of quadratic equation if discriminant>=0'''
    rootlist = []
    if discriminant > 0:
        rootlist.append((-b + sqrt(discriminant)) / (2 * a))
        rootlist.append((-b - sqrt(discriminant)) / (2 * a))
    elif discriminant == 0:
        rootlist.append(-b / (2 * a))
    return rootlist


# Create your views here.
def quadratic_results(request):
    D = x1 = x2 = message = ''
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            D = discriminant(a, b, c)
            if D >= 0:  # calc roots
                try:
                    x1, x2 = roots(D, a, b)  # > 0
                    message='Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)
                except ValueError:
                    x1 = roots(D, values_dict['a'], values_dict['b'])[0]  # = 0
                    message='Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x1)
            else:
                message='Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        form = QuadraticForm()

    context = {'discriminant': D,
               'message': message,
               'form': form,
               }
    return render(request, 'results.html', context)
