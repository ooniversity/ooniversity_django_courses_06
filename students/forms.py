#coding: utf-8 
from django import forms
from django.db import models
from students.models import Student


class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
