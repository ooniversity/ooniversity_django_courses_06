from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):

    context = {}
    info = ''
    diskr = ''
    flag = False

    if request.method == "GET":
        form = QuadraticForm(request.GET)
        if form.is_valid():
            
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            context['diskr'] = b**2 - 4*a*c

            if context['diskr'] < 0:
                context['flag'] = True
                context['info'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif context['diskr'] == 0:
                context['flag'] = True
                x1 = x2 = (b + context['diskr'] ** (1/2.0)) / 2*a
                context['info'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" %x1
            elif context['diskr'] > 0:
                context['flag'] = True
                x1 = (-b + context['diskr'] ** (1/2.0)) / 2*a
                x2 = (-b - context['diskr'] ** (1/2.0)) / 2*a
                context['info'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1, x2)     

    else:
        form = QuadraticForm()
    context['form'] = form
    return render(request, 'quadratic/results.html', context)
