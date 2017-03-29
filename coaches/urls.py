from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = 'coaches'

urlpatterns = [
	url(r'^(?P<coach_id>[0-9]+)/$', views.detail, name='detail'),
]
