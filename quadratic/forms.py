from django import forms

class QuadraticForm(forms.Form):

    a = forms.IntegerField(label="коэффициент a")
    b = forms.IntegerField(label="коэффициент b")
    c = forms.IntegerField(label="коэффициент c")

    def clean_a(self):
        value_a = self.cleaned_data['a']
        if value_a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

        return value_a

