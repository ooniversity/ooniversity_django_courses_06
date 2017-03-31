from django.conf.urls import url
from . import views

app_name = 'quadratic'
urlpatterns = [
#	url(r'^/$', views.quadratic_results, name='results'),
	url(r'^results/', views.quadratic_results, name='results'),
]