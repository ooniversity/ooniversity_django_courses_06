from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import math
from django.contrib import messages
from . forms import QuadraticForm
# Create your views here.

 

def quadratic_results(request):
    deskr = None
    message = None
    if request.method == "POST":
        form = QuadraticForm(request.POST)
        
        
        if form.is_valid():
            data = form.cleaned_data
            a = form.clean_a()
            b = data['b']
            c = data['c']
            
            
            deskr = b ** 2 - 4 * a * c
           
            if deskr < 0:
                message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
                
            elif deskr == 0:
                x = (-b + math.sqrt(deskr)) / (2 * a)
                message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %d' % (x)
                
            else:
                x1 = -b + math.sqrt(deskr) / (2 * a)
                x2 = -b - math.sqrt(deskr) / (2 * a)
                
                message = 'Квадратное уравнение имеет два действительных корня: x1 = %d, x2 = %d' % (x1, x2)
            messages.success(request, 'Дискриминант: {}'.format(deskr))
            messages.success(request, message)
    else:
        form = QuadraticForm()
        #context = {'form': form, 'message':message}
    return render(request, 'quadratic/results.html', {'form':form})






def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def student_list(request):
    return render(request, "student_list.html")

def student_detail(request):
    return render(request, "student_detail.html")
    
