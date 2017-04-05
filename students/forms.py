from students.models import Student
from django import forms 

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']




