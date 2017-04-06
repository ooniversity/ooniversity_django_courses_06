from django.conf.urls import url
from . import views

app_name = 'students'

urlpatterns = [

    #url(r'edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),

    #url(r'remove/(?P<id>\d+)/$', views.remove, name='remove'),
    url(r'remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),


    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    #url(r'(\d)+/$', views.detail, name='detail'),

    #url(r'(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),

    #url(r'(?P<course_id>[0-9]+)/$', views.list_view, name='list_view'),
    #url(r'(?P<course_id>[0-9]+)/$', views.StudentListView.as_view(), name='list_view'),

    #url(r'add/$', views.create, name='add'),
    url(r'add/$', views.StudentCreateView.as_view(), name='add')
]
