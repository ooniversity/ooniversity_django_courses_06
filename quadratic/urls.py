from django.conf.urls import include, url
from django.contrib import admin
from . import views




urlpatterns = [
    
    url(r'^results/$', views.quadratic_results, name='quadratic_results'),
    
]
