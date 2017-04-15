from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from coaches.models import Coach
from django import forms
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


import logging
logger = logging.getLogger(__name__)

class CourseDetailView(DetailView):
	model = Course
	template_name = 'courses/detail.html'
	context_object_name = 'course'

	def get_queryset(self):
		qs = super().get_queryset()
		course_id = self.request.GET.get('pk', None)
		if course_id:
			qs = qs.filter(courses=course_id)
		return qs

	def get_context_data(self, **kwargs):
		logger.debug('Courses detail view has been debugged!')
		logger.info('Logger of courses detail view informs you!')
		logger.warning('Logger of courses detail view warns you!')
		logger.error('Courses detail view went wrong!')
		context = super().get_context_data(**kwargs)
		context['lessons'] = Lesson.objects.filter(course=self.object.pk)
		context['course'] = Course.objects.get(id=self.object.pk)
		return context

class CourseCreateView(CreateView):
	model = Course
	template_name = 'courses/add.html'
	success_url = reverse_lazy('index')
	form_class = CourseModelForm
	context_object_name = 'course'

	def form_valid(self, form):
		response = super().form_valid(form)
		messages.success(self.request, "Course {} has been successfully added.".format(self.object.name))
		return response

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Course creation'
		return context

class CourseUpdateView(UpdateView):
	model = Course
	template_name = 'courses/edit.html'
	form_class = CourseModelForm
	context_object_name = 'course'

	def get_success_url(self):
		return reverse('courses:edit', args=(self.object.pk,))

	def form_valid(self, form):
		response = super().form_valid(form)
		messages.success(self.request, "The changes have been saved.")
		return response

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Course update'
		return context


class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'courses/remove.html'
	success_url = reverse_lazy('index')
	form_class = CourseModelForm
	context_object_name = 'course'

	def delete(self, request, *args, **kwargs):
		response = super().delete(request, *args, **kwargs)
		messages.success(self.request, "Course {} has been deleted.".format(self.object.name))
		return response

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Course deletion'
		return context

def add_lesson(request, course_id):
	if request.method == "POST":
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			messages.success(request, "Lesson {} has been successfully added.".format(lesson.subject))
			return redirect('courses:detail', lesson.course.id)
	else:
		course = Course.objects.get(id=course_id)
		form = LessonModelForm(initial={'course': course})
	return render(request, 'courses/add_lesson.html', {'form': form})
