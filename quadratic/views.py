from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):

    context = {}
    info = ''
    diskr_value = ''


    if request.method == "GET":
        form = QuadraticForm(request.GET)
        if form.is_valid():
            
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            context['diskr_value'] = b**2 - 4*a*c
            context['diskriminant'] = 'Дискриминант: '
            if context['diskr_value'] < 0:

                context['info'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif context['diskr_value'] == 0:

                x1 = x2 = (b + context['diskr_value'] ** (1/2.0)) / 2*a
                context['info'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" %x1
            elif context['diskr_value'] > 0:

                x1 = (-b + context['diskr_value'] ** (1/2.0)) / 2*a
                x2 = (-b - context['diskr_value'] ** (1/2.0)) / 2*a
                context['info'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1, x2)     

    else:
        form = QuadraticForm()
    context['form'] = form
    return render(request, 'quadratic/results.html', context)
