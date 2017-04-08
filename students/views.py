from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from students.forms import StudentModelForm
from students.models import Student
from courses.models import Course


# Create your views here.
class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TechBursa Python/Django 06 :: Students - DetailView'
        return context


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.request.GET.get('course_id')
        if pk:
            course = get_object_or_404(Course, id=pk or 0)
            qs = Student.objects.filter(courses__id=pk)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'TechBursa Python/Django 06 :: Students - list'
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def form_valid(self, form):
        response = super().form_valid(form)
        fieldsets = form.cleaned_data
        messages.success(self.request,
                         "Student {} {} has been successfully added.".format(fieldsets['name'], fieldsets['surname']))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = " Student registration"
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:edit')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        qs=self.object
        messages.success(request, "Info on {} {} has been successfully deleted.".format(qs.name, qs.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context
