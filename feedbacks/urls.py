from django.conf.urls import url
from feedbacks import views


urlpatterns = [
	url(r'^$', views.FeedbackView.as_view(), name='feedback'),
]
