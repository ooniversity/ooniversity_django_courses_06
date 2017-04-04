from django.conf.urls import include, url

from . import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='create'),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove, name='remove'),
]