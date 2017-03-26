from django.conf.urls import url, include
from courses import views 


app_name = 'courses'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
]
