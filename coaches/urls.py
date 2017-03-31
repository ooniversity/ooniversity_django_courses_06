from django.conf.urls import url

from . import views

app_name = 'coaches'

urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]