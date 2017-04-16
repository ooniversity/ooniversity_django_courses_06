from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label="коэффициент a", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    b = forms.IntegerField(label="коэффициент b", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    c = forms.IntegerField(label="коэффициент c", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_a(self):
        a = self.cleaned_data['a']

        if a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

        return a
