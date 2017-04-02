from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='create'),
    url(r'^add_lesson/(?P<id>\d+)/$', views.add_lesson, name='add_lesson'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),

]