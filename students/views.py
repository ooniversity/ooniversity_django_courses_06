from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from django import forms
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


import logging
logger = logging.getLogger(__name__)


class StudentListView(ListView):
	model = Student
	template_name = 'students/list.html'
	context_object_name = 'students_list'
	paginate_by = 2

	def get_queryset(self):
		qs = super().get_queryset()
		course_id = self.request.GET.get('course_id')
		if course_id:
			qs = qs.filter(courses__id=course_id)
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class StudentDetailView(DetailView):
	model = Student
	template_name = 'students/detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Student detail'
		logger.debug('Studens detail view has been debugged!')
		logger.info('Logger of students detail view informs you!')
		logger.warning('Logger of students detail view warns you!')
		logger.error('Students detail view went wrong!')
		return context


class StudentCreateView(CreateView):
	model = Student
	template_name = 'students/add.html'
	success_url = reverse_lazy('students:list_view')
	form_class = StudentModelForm

	def form_valid(self, form):
		response = super().form_valid(form)
		messages.success(self.request, "Student {} has been successfully added.".format(self.object.full_name()))
		return response

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Student registration'
		return context


class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/edit.html'
	success_url = reverse_lazy('students:list_view')
	form_class = StudentModelForm

	def form_valid(self, form):
		response = super().form_valid(form)
		messages.success(self.request, "Info on the student has been successfully changed.")
		return response

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Student info update'
		return context


class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/remove.html'
	success_url = reverse_lazy('students:list_view')
	form_class = StudentModelForm

	def delete(self, request, *args, **kwargs):
		response = super().delete(request, *args, **kwargs)
		messages.success(self.request, "Info on {} has been successfully deleted.".format(self.object.full_name()))
		return response

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Student info suppression'
		return context
