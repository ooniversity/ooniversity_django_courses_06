from django.conf.urls import url
from students.views import list_view, create, edit, remove, detail 


app_name = 'students'
urlpatterns = [
    url(r'^$', list_view, name='list_view'),
    url(r'^add/$', create, name='create'),
    url(r'^edit/(?P<student_id>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', remove, name='remove'),   
    url(r'^(?P<student_id>\d+)/$', detail, name='detail'),
]
