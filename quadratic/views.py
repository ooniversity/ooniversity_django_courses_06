from django.shortcuts import render
from quadratic.forms import QuadraticForm



def quadratic_results(request):
    if len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        context = {}
        context["form"] = form
        context["diskr"] = ''
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            diskr = b * b - 4 * a * c
            context['diskr'] = "Дискриминант: %s" %diskr
            if diskr < 0:
                context["info"] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif diskr == 0:
                x1 = -b / 2 * a
                context['info'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" %x1
            else:
                x1 = (-b + diskr ** (1 / 2)) / 2 * a
                x2 = (-b - diskr ** (1 / 2)) / 2 * a
                context['info'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" %(x1, x2) 
    else:
        form = QuadraticForm()
        context = {'form': form}
    return render(request, 'quadratic/results.html', context)


