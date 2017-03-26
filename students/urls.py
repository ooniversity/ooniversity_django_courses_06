from django.conf.urls import url
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    #url(r'^(?P<cid>[0-9]+)/$', views.list_view, name='list-view'),
    url(r'^(?P<sid>[0-9]+)/$', views.detail, name='detail'),# 
]