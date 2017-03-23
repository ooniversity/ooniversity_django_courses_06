from django.conf.urls import url
from . import views

app_name = 'students'

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'(?P<course_id>[0-9]+)/$', views.list, name='list'),
    url(r'^(\d+)$', views.detail, name='detail'),

]