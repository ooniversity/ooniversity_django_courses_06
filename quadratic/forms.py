from django import forms


class QuadraticForm(forms.Form):
	a = forms.CharField(label='коэффициент a', max_length=5)
	b = forms.CharField(label='коэффициент b', max_length=5)
	c = forms.CharField(label='коэффициент c', max_length=5)

	def clean_a(self):
		data = self.cleaned_data['a']
		if data == 0:
			raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")

		return data
