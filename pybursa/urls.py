from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^feedback/', include('feedbacks.urls')),
    url(r'^admin/', admin.site.urls),
]
