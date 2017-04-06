from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django import forms
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

class StudentDetailView(DetailView):
    model =  Student
    template_name = 'students/detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['title'] = "Данные скубента"
        return context


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'studentsList'

    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()

        if 'course_id' in self.request.GET:
            qs = qs.filter(courses__id=self.request.GET['course_id'])
        return qs

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['title'] = " Список скубентов. "
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/add.html'
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super(StudentCreateView, self).form_valid(form)
        messages.success(self.request, "Info on %s has been successfully added." %(self.object.full_name()))
        return response

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = " Student registration "
        return context



class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    template_name = 'students/remove.html'
    success_message = "Info on %(name)s %(surname)s has been successfully deleted."

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, self.success_message % obj.__dict__)
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class =  StudentModelForm
    template_name = 'students/edit.html'

    def get_success_url(self, **kwargs):
    	print(self.kwargs)
    	return reverse_lazy('students:edit', args = (self.kwargs['pk']))

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return response

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context
