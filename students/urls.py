from django.conf.urls import url, include
from django.contrib import admin
from students import views
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

app_name = 'students'
urlpatterns = [
	url(r'^$', views.StudentListView.as_view(), name='list_view'),
	url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
	url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
	url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
	url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
]
