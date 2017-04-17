from django.shortcuts import render,redirect
from . models import Student
from courses.models import Course
from django import forms
from . forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


import logging
logger = logging.getLogger(__name__) #pybursa.views

class StudentListView(ListView):
	model = Student
	#template_name = 'students/list.html'
	context_object_name = 'students_list'
	paginate_by = 2

	def get_queryset(self):
		qs = super().get_queryset()
		course_id = self.request.GET.get('course_id')
		if course_id:
			qs = qs.filter(courses_id=course_id)
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


#def list_view(request):
#    data = request.GET
#
#    if data:
#        course_id = data['course_id']
#        course = Course.objects.get(id=course_id)
#        students_list = Student.objects.filter(courses__id=course_id)
#
#        context = {
#            'students_list': students_list,
#            'current_course': course,
#        }
#    else:
#        students_list = Student.objects.all()
#        context = {
#            'students_list': students_list
#        }
#
#    return render(request, 'students/list.html', context)


class StudentDetailView(DetailView):
	model = Student

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		logger.debug("Students detail view has been debugged!")
		logger.info("Logger of students detail view informs you!")
		logger.warning("Logger of students detail view warns you!")
		logger.error("Students detail view went wrong!")
		context['title'] = "Student detailed info"
		return context
	#template_name = 'students/detail.html'

#def detail(request, student_id):
#   student = Student.objects.get(id=student_id)
#
#    context = {
#        'student': student
#    }
#
#    return render(request, 'students/detail.html', context)


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    #template_name = 'students/add.html'
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student %s %s has been successfully added." % (self.object.name, self.object.surname))
        return response

#def add(request):
#	if request.method == 'POST':
#		form = StudentModelForm(request.POST)
#		if form.is_valid():
#			student = form.save()
#			message = u"Student %s %s has been successfully added." %(student.name, student.surname)
#			messages.success(request, message)
#			return redirect('students:list_view')
#	else:
#		form = StudentModelForm()
#
#	return render(request, 'students/add.html', {'form':form})


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')
    #template_name = 'students/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Info on %s %s the student has been successfully changed.'% (self.object.name, self.object.surname))
        return response


#def edit(request,id):
#	student_inst=Student.objects.get(pk=id)
#	if request.method == 'POST':
#		form = StudentModelForm(request.POST, instance=student_inst)
#		if form.is_valid():
#			student= form.save()
#			message = u"Info on %s %s the student has been sucessfully changed." %(student.name, student.surname)
#			messages.success(request, message)
#			return redirect('students:list_view')
#	else:
#		form = StudentModelForm(instance=student_inst)
#
#	return render(request,"students/edit.html",{"form":form})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    #template_name = 'students/remove.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(self, request, *args, **kwargs)
        messages.success(self.request, 'Info on %s %s the student has been sucessfully deleted.'% (self.object.name, self.object.surname))
        return response

#def remove(request,id):
#	student=Student.objects.get(pk=id)
#	if request.method == 'POST':
#		student.delete()
#		message = u"Info on %s %s has been sucessfully deleted." %(student.name, student.surname)
#		messages.success(request, message)
#		return redirect('students:list_view')
#	return render(request,"students/remove.html",{"student":student})
