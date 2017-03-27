from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = 'PyBursa Administration'

urlpatterns = [
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls'))
]