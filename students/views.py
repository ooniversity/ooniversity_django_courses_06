from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class StudentDetailView(DetailView):
    model =  Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Данные скубента"
        return context


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name =  'students'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        if 'course_id' in self.request.GET:
            qs = qs.filter(courses__id=self.request.GET['course_id'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'course_id' in self.request.GET:
            context['courseId'] = self.request.GET['course_id']
        context['title'] = " Список скубентов. "
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student %s has been successfully added." %(self.object.full_name()))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = " Student registration"
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        studentname = self.object.full_name()
        messages.success(request, "Info on %s has been successfully deleted." %(self.object.full_name()))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context


class StudentUpdateView(UpdateView):
    model = Student
    form_class =  StudentModelForm
    success_url = reverse_lazy('students:list_view')
    
#    def get_success_url(self, **kwargs):
#    	return reverse_lazy('students:edit', args = (self.kwargs['pk']))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context