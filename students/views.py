from django.shortcuts import render, redirect, reverse
from . models import Student
from courses.models import Course
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)
                   
        return qs

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Some name' 
        return context'''


'''def list_view(request):
    data = request.GET
    course = None
    if data:
        course_id = data['course_id']
        course = Course.objects.get(id=course_id)
        students_list = Student.objects.filter(courses__id=course_id)
    else:
        students_list = Student.objects.all()
    
    return render(request, 'students/list.html', {'students_list':students_list, 'current_course': course})'''


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student registration'
        context['title'] = 'Student registration'
        context['button_name'] = 'Add'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student {} {} been successfully added.'.format(self.object.name, self.object.surname))
        return response


'''def create(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            messages.success(request, 'Student {}{} has been successfully added.'.format(data['name'], data['surname']))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form':form})'''

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student info update'
        context['title'] = 'Student info update' 
        context['button_name'] = 'Save'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on the {} {} has been successfully changed.'.format(self.object.name, self.object.surname))
        return response




"""def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            data = form.cleaned_data
            
            student.save()
            messages.success(request, 'Info on the student has been successfully changed.')
            return redirect('students:detail', pk)
    else:
        form = StudentModelForm(instance=student)

    
    
    return render(request, "students/edit.html", {'form':form})"""

class StudentDeleteView(DeleteView):
    model = Student
    #form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Student info suppression'
        context['title'] = 'Student info suppression' 
        return context
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Info on {} {} has been successfully deleted'.format(self.object.name, self.object.surname))
        return response




'''def remove(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == "POST":
                
            
            messages.success(request, 'Info on {} {} has been successfully deleted'.format(student.name, student.surname))
            student.delete()
            return redirect('students:list_view')
    else:
        form = StudentModelForm(instance=student)

    
    
    return render(request, "students/remove.html", {'student':student})'''




