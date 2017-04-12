from . import views
from django.conf.urls import url

app_name = 'coaches'

urlpatterns = [url(r'^(?P<coach_id>\d+)/$', views.detail, name='detail'),]