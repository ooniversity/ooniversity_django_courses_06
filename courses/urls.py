from django.conf.urls import url, include
from courses import views 


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
]
