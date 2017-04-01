from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from . forms import QuadraticForm

import math

def quadratic_results(request):
    data = request.GET

    if not data:
        form = QuadraticForm()
    else:
        form = QuadraticForm(request.GET)

        if form.is_valid():
            data = form.cleaned_data

            A = data['a']
            B = data['b']
            C = data['c']

            D = B**2 - 4*A*C

            if D < 0:
                message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif D == 0:
                x = -B/(2*A)
                message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x)
            else:
                x1 = (-B + math.sqrt(B**2 - 4*A*C)) / (2*A)
                x2 = (-B - math.sqrt(B**2 - 4*A*C)) / (2*A)
                message = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x1, x2)

            messages.success(request, 'Дискриминант: {}'.format(D))
            messages.success(request, message)

    return render(request, 'results.html', {'form': form})
