from django.conf.urls import include, url
from django.contrib import admin
from pybursa.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contact', contact, name='contact'),
    url(r'^student_list', student_list, name='student_list'),
    url(r'^student_detail', student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^quadratic/', include('quadratic.urls')),
]
