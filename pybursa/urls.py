from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views 
#from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^courses/', include('courses.urls', namespace='courses')),    
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
]

admin.site.site_header = 'PyBursa Administration'
