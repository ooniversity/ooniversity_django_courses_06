from django.conf.urls import url
from quadratic.views import quadratic_results

urlpatterns = [
    url(r'^$', quadratic_results, name='quadratic_results'),
]