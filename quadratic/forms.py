from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a', localize=True)
    b = forms.IntegerField(label='коэффициент b', localize=True)
    c = forms.IntegerField(label='коэффициент c', localize=True)

    def clean_a(self):
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return a
