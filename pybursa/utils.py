from django.shortcuts import render

def detail_view(request, pk, obj_class):
    obj_name = obj_class.__name_.lower()
    obj 
