from django.conf.urls import url

from . import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(\d+)/$', views.detail, name='detail'),
]