from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),

    #url(r'remove/(?P<id>\d+)/$', views.remove, name='remove'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDelete.as_view(), name='remove'),

    #url(r'edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),

    #url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),

    #url(r'add/$', views.add, name='add'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),

]