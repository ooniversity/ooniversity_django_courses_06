from django.conf.urls import url

from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<student_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<student_id>[0-9]+)/$', views.remove, name='remove'),
]
