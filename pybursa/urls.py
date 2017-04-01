from django.conf.urls import include, url
from django.contrib import admin
from . import views 
from .views import index, contact, student_list, student_detail

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^courses/', include('courses.urls', namespace='courses')),    
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
]

admin.site.site_header = 'PyBursa Administration'
