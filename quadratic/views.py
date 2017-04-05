from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import math
from django.contrib import messages
from . forms import QuadraticForm
# Create your views here.

 

def quadratic_results(request):
    message = {}
    diskr = ''
    if request.method == "GET":
        form = QuadraticForm(request.GET)
        
        
        if form.is_valid():
            data = form.cleaned_data
            a = form.clean_a()
            b = data['b']
            c = data['c']
            
            
            deskr = b ** 2 - 4 * a * c
            diskr = "Дискриминант: {}".format(deskr)
            if deskr < 0:
                message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
                
            elif deskr == 0:
                x = (-b + math.sqrt(deskr)) / (2 * a)
                message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(round(x))
            else:
                x1 = -b + math.sqrt(deskr) / (2 * a)
                x2 = -b - math.sqrt(deskr) / (2 * a)
                
                message = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(round(x1), round(x2))
            
    else:
        form = QuadraticForm()
        #context = {'form': form, 'message':message}
    return render(request, 'quadratic/results.html', {'form':form, 'message': message, 'diskr':diskr})






'''def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")'''
    
