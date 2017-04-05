from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns =[
    url(r'^',views.list_courses,name ='list_of_courses'),
    url(r'^courses/<a>',views.lessons_list,name = 'lessons_list'),
]
