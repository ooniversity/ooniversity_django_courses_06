from django.shortcuts import render
from django.http import HttpResponse
from quadratic.forms import QuadraticForm
import math

def quadratic_results(request):
    form = QuadraticForm()
#    context['form']=form
    return render(request, 'quadratic/results.html', {'form':form})
 
"""    def check_int(str):
        try:
            int(str)
            return True
        except:
            return False

    coefA = request.GET.get('a', None)
    coefB = request.GET.get('b', None)
    coefC = request.GET.get('c', None)

    koefA = koefB = koefC = a = b = c = discrim = mainresult = ""
    a = b = c = ""
    isCorrect = True

    if coefA == "":
        koefA = "коэффициент не определен"
        isCorrect = False
    else:
        if coefA =='0':
            a = 0
            koefA = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
            isCorrect = False
        else:
            a = int(coefA)
        
    if coefB == "":
        koefB = "коэффициент не определен"
        isCorrect = False
    else:
        if check_int(coefB):
            b = int(coefB)
        else:
            b = coefB
            koefB = "коэффициент не целое число"
            isCorrect = False

    if coefC == "":
        koefC = "коэффициент не определен"
        isCorrect = False
    else:
        if check_int(coefC):
            c = int(coefC)
        else:
            c = coefC
            koefC = "коэффициент не целое число"
            isCorrect = False

    if isCorrect:
        discrim = b**2 -4*a*c
        if discrim < 0:
            mainresult = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        if discrim == 0:
            mainresult = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = "+str(-b/(2*a))
        if discrim >0 :
            mainresult = "Квадратное уравнение имеет два действительных корня: x1 = "+str((-b + math.sqrt(discrim)) / (2*a))+", x2= "+str((-b - math.sqrt(discrim)) / (2*a))
        
    
    return render(request, 'quadratic/results.html', 
        { "a": a,
          "b": b,
          "c": c,
          "koefA" :koefA,
          "koefB" :koefB,
          "koefC" :koefC,
          "isCorrect": isCorrect,
          "discrim" : discrim,
          "mainresult" :mainresult,
        
        })


    """
