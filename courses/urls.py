from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns =[
    url(r'^',views.list_courses,name ='courses'),
    url(r'^(?P<pk>\d+)/$',views.details,name = 'details'),
]
