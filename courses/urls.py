from django.conf.urls import url

from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/(\d+)/$', views.detail, name='detail'),
]