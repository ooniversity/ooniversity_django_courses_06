from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from students.forms import StudentModelForm
from students.models import Student
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)

        if course_id:
            qs = qs.filter(courses__id=course_id)

        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        message = "Student %(name)s %(surname)s has been successfully added." % {
            'name': self.object.name,
            'surname': self.object.surname
            }
        messages.success(self.request, message)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        message = "Info on the student has been successfully changed."
        messages.success(self.request, message)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('students:edit', args=(pk,))


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        message = "Info on %(name)s %(surname)s has been successfully deleted." % {
            'name': self.object.name,
            'surname': self.object.surname
        }
        messages.success(self.request, message)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
