from django.conf.urls import include, url
from django.contrib import admin
from pybursa import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^feedback/', include('feedbacks.urls')),
]

admin.site.site_header = 'PyBursa Administration'

from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]