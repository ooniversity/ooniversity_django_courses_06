from django import forms

# Register your models here.
def isint(value):
    try:
        # print("!!!we in tray!!! ",key," : ",kwargs.get(key))
        int(value)
        result = True
    except ValueError:
        result = False
    
    return result

class QuadraticForm(forms.Form):
    a = forms.CharField(label='коэффициент a', max_length=8)
    b = forms.CharField(label='коэффициент b', max_length=8)
    c = forms.CharField(label='коэффициент c', max_length=8)
    
    def clean_a(self):
        data = self.cleaned_data['a']
        print('data=',data)
        if data == '0':
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
        elif not isint(data):
            raise forms.ValidationError("коэффициент не целое число")
        return data