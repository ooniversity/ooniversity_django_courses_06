from django.conf.urls import url
from courses.views import add, edit, remove, add_lesson, detail


app_name = 'courses'
urlpatterns = [
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', remove, name='remove'),
    url(r'^(?P<id>\d+)/add_lesson/$', add_lesson, name='add-lesson'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
]
