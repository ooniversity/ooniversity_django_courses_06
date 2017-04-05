from django.shortcuts import render
from courses.models import Course, Lesson
from django.views.generic.base import TemplateView
from django.views.decorators.cache import cache_page


class CoursesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class IndexView(CoursesMixin, TemplateView):
    template_name = 'index.html'


@cache_page(5)
def index(request):
    print("INDEX")
    courses = Course.objects.all()
    return render(request, "index.html", {"courses": courses})


class ContactView(CoursesMixin, TemplateView):
    template_name = 'contact.html'