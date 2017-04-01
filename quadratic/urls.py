from django.conf.urls import url
from . import views

#app_name = 'quadratic'
urlpatterns = [
#	url(r'^$', quadratic_results, name='quadratic_results'),
	url(r'^results/$', views.quadratic_results, name='quadratic_results'),
]