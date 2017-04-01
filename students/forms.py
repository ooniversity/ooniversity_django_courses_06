from django import forms
from students.models import Student

"""
class StudentAdd(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    skype = forms.CharField(max_length=255)
    #courses = forms.ManyToManyField(Course, related_name='course')
"""

class StudentModelForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'surname', 'date_of_birth', 'email', 
		          'phone', 'address', 'skype', 'courses']