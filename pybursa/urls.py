"""pybursa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
#from pybursa import views
from .views import index, contact, student_list, student_detail
from quadratic.views import quadratic_results
from feedbacks import views
from django.views.defaults import server_error, page_not_found, permission_denied

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contact/',  contact, name='contact'),
    url(r'^feedback/',  views.FeedbackView.as_view(), name='feedback'),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^courses/', include('courses.urls', namespace = 'courses', app_name='courses')),
    url(r'^students/', include('students.urls', namespace = 'students', app_name='students')),
    url(r'^coaches/', include('coaches.urls', namespace = 'coaches', app_name='coaches')),
    url(r'^admin/', admin.site.urls),
]

#handler404 = curry(page_not_found, template_name='404.html')
#handler500 = curry(server_error, template_name='500.html')

#handler404 = views.handler404
#handler500 = views.handler500
