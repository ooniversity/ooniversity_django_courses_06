from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a', initial = 1)
    b = forms.IntegerField(label='коэффициент b', initial = 1)
    c = forms.IntegerField(label='коэффициент c', initial = 1)

#    def clean_a (self):
#    	data = self.cleaned_data['a']

