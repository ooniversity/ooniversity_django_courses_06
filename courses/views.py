from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django import forms
from django.contrib import messages


def detail(request, pk):
    context = {'course': Course.objects.get(id=pk), 
               'lessons': Lesson.objects.filter(course=pk)}
    return render(request, "courses/detail.html", context)

class CourseApplyForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    description = forms.CharField(label="short description", max_length=255)
    level = forms.ChoiceField(choices=(('hard', 'Hard'),
                                       ('easy', 'Easy'),
                                       ('standart', 'Standart')),
                                       widget=forms.RadioSelect)
    non_sleep_mode = forms.BooleanField(help_text="hello")
