from django.conf.urls import url
from django.http import HttpResponse

from .views import quadratic_results


def index(request):
    return HttpResponse("<h1>Quadratic equation</h1>")

urlpatterns = [
    url(r'^$', index),
    url(r'^results/', quadratic_results, name='results'),
]
