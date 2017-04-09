from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django import forms
from django.core.urlresolvers import reverse 
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id')
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'STUDENTS' 
        course_id = self.request.GET.get('course_id')
        context['course_id'] = '?course_id=%s&' %course_id if course_id else ''
        return context


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student %s has been successfully added." %self.object.full_name())

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student registration"
        context['page_header'] = "Создание нового студента"
        return context


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        print()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        context['page_header'] = "Редактирование студента"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Info on %s has been successfully deleted." %self.object.full_name())
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context