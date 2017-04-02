from django import forms
from . models import Course, Lesson

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        # fields = ['name', 'short_description', 'description', 'coach', 'assistant']

        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'short_description': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'coach': forms.Select(attrs={'class': 'form-control'}),
        #     'assistant': forms.Select(attrs={'class': 'form-control'}),
        # }


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson

        fields = '__all__'

        # fields = ['subject', 'description', 'course', 'order']

        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'course': forms.Select(attrs={'class': 'form-control'}),
        #     'order': forms.NumberInput(attrs={'class': 'form-control'}),
        # }