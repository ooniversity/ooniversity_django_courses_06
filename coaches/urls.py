from django.conf.urls import url

from . import views

app_name = 'coaches'
urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]
