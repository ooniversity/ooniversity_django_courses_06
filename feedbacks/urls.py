from django.conf.urls import url

from . import views

#app_name = 'quadratic'
urlpatterns = [
    url(r'^$', views.FeedbackView.as_view(), name='feedback'),
]