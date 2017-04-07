from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=pk).order_by('order')
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course {0} has been successfully added.'.format(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    form_class = CourseModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('courses:edit', args=(pk,))


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/remove.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Course {0} has been deleted.'.format(self.object.name))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context


def add_lesson(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Lesson {0} has been successfully added.".format(instance.subject))
            url_string = reverse('courses:detail', args=(course_id,))
            return redirect(reverse('courses:detail', args=(course_id,)))
    else:
        form = LessonModelForm(initial={'course': course})
    return render(request, 'courses/add_lesson.html', {'form': form})
