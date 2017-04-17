
# encoding: utf-8
from django.shortcuts import redirect
from django.shortcuts import render

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


import logging
logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context["lessons"] = Lesson.objects.filter(course_id = self.object)
        context['course'] = Course.objects.get(id=self.object.pk)
        logger.debug("Courses detail view has been debugged")
        logger.info("Logger of courses detail view informs you!")
        logger.warning("Logger of courses detail view warns you!")
        logger.error("Courses detail view went wrong!")
        return context


class CourseCreateView(CreateView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/add.html'
    success_url = reverse_lazy('index')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView,self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context

    def form_valid(self, form):
        application = form.save()
        msg = u"Course %s has been successfully added." % (application.name)
        messages.success(self.request, msg)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/edit.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = u"Course update"
        return context

    def get_success_url(self):
        return reverse_lazy('courses:edit', args=(self.object.id,))

    def form_valid(self, form):
        application = form.save()
        messages.success(
            self.request, u"The changes have been saved.")
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/remove.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = u"Course deletion"
        context['notice'] = u"The cource %s will be removed" % (
            self.object.name)
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request, 'Course {} has been deleted.'.format(self.get_object()))
        return super(CourseDeleteView, self).delete(self, request, *args, **kwargs)


class LessonCreateView(SuccessMessageMixin, CreateView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'courses/add_lesson.html'
    success_url = reverse_lazy('courses:detail')
    success_message = "%(subject)s was created successfully"

    def get(self, request, *args, **kwargs):
        course=Course.objects.get(pk=kwargs['pk'])
        form = LessonModelForm(initial = {'course': course.id})
        return render(request, self.template_name , {"form":form})

    def get_success_url(self):
        return reverse_lazy('courses:detail', kwargs={'pk': self.object.course.id})

    def get_context_data(self, **kwargs):
        context = super(LessonCreateView, self).get_context_data(**kwargs)
        context['title'] = u"Lesson creation"
        return context
