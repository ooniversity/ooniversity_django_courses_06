from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'students'
urlpatterns = [
	url(r'^$', views.list_view, name='list_view'),
	url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
]
