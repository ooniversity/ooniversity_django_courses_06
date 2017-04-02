from django import forms
from . models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'skype': forms.TextInput(attrs={'class': 'form-control'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

        help_texts = {
            'courses': 'Hold down "Control", or "Command" on a Mac, to select more than one.',
        }
