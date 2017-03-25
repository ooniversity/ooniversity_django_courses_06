from django.conf.urls import url

from . import views


app_name = 'students'
urlpatterns = [
	url(r'^$', views.students, name='student_list'),
    url(r'^(?P<student_id>[0-9]+)/$', views.student_detail, name='student_detail'),
]
