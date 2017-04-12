from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'(?P<pk>\d+)/add_lesson$', views.LessonCreateView.as_view(), name='add-lesson'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),

]