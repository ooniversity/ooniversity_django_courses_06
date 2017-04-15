from django.shortcuts import render, redirect, get_object_or_404
from students.models import Student
from .forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import logging

logger = logging.getLogger('students')


class StudentListView(ListView):
    model = Student
    paginate_by = 2
 
    def get_queryset(self):
       qs = super().get_queryset()
       course_id = self.request.GET.get('course_id', None)
       if course_id:
           qs = qs.filter(courses__id=course_id)
       return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            context['course_id_url'] = 'course_id={}&'.format(self.request.GET.get('course_id', None)) 
        return context

class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug("Students detail view has been debugged!")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student {0} has been successfully added.".format(form.cleaned_data['name'] + ' ' + form.cleaned_data['surname']))
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration' 
        return context
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    
    def get_success_url(self):
        super().get_success_url()
        pk = self.kwargs['pk']
        return reverse('students:edit', args=(pk,))

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
    success_url = reverse_lazy('students:list_view')
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, "Info on {0} has been successfully deleted.".format(
            self.object.name + ' ' + self.object.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression' 
        return context

