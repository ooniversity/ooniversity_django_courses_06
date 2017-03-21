from django.shortcuts import render
from django.http import HttpResponse
from quadratic.quadratic_handler import QuadraticEducation
# Create your views here.

def results(request,a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    render()


def check_paramtr(name):
    while True:
        p = input("Enter the parametr of equation %s = "% name)
        if p.replace('.','').isdigit()and float(p )!= 0:
            p = float(p)
            return p
        else:
            print("Please enter the number of nonzero !")