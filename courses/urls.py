from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^add/', views.add, name='add'),
    url(r'^add/(?P<id>\d+)/add_lesson', views.add_lesson, name='add-lesson'),
    url(r'^remove/(?P<id>\d+)/', views.remove, name='remove'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
]