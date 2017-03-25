from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^(?P<cid>[0-9]+)/$', views.detail, name='detail'),
]