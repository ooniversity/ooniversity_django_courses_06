from django.shortcuts import render
from math import sqrt
from django.http import QueryDict
from quadratic.forms import QuadraticForm

class Coefficient(object):

	def __init__(self, name, value):
		self.name = name
		self.value = value
		self.value_int = None
		self.error_message = None

	def is_valid(self):
		if not self.value:
			self.error_message = "коэффициент не определен"
			return False

		try:
			self.value_int = int(self.value)
		except ValueError:
			self.error_message = "коэффициент не целое число"
			return False

		if self.name == 'a' and self.value_int == 0:
			self.error_message = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
			return False
		return True

def get_discr(a, b, c):
	d = b**2 - 4*a*c
	return d

def get_eq_root(a, b, d, order=1):
	if order == 1:
		x = (-b + d**(1/2.0)) / 2*a
	else:
		x = (-b - d**(1/2.0)) / 2*a
	return x

def quadratic_results(request):
	form = QuadraticForm()
	context = {'error': False}
	context['form'] = form
	for name_value in ['a', 'b', 'c']:
		coefficient = Coefficient(name_value, request.GET.get(name_value, ''))
		if coefficient.is_valid():
			context[name_value] = coefficient.value_int
		else:
			context['error'] = True
			context[name_value + '_error'] = coefficient.error_message
			context[name_value] = coefficient.value
	if not context['error']:
		a = context['a']
		b = context['b']
		c = context['c']
		d = get_discr(a, b, c)
		if d < 0:
			result_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
		elif d == 0:
			x = get_eq_root(a, b, d)
			result_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}'.format(x)
		else:
			x1 = get_eq_root(a, b, d)
			x2 = get_eq_root(a, b, d, order=2)
			result_message = 'Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}'.format(x1, x2)

		context.update({'d': d, 'result_message': result_message})
	return render(request, 'results.html', context)

#def quadratic_results(request):
#    def try_int(data):
#        my_int = data
#        if data == '':
#            res = 'коэффициент не определен'
#        else:
#            try: 
#                my_int = int(data)
#                res = ''           
#            except: 
#                res = 'коэффициент не целое число'
#        return res, my_int 
       
#    url_data = request.GET
#    a = url_data['a'] if url_data.__contains__('a') else ''
#    b = url_data['b'] if url_data.__contains__('b') else ''
#    c = url_data['c'] if url_data.__contains__('c') else ''
#    res_a, a = try_int(a)                                       
#    res_b, b = try_int(b)   
#    res_c, c = try_int(c) 
#    if a == 0:
#        res_a = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
#        my_discr = ''
#        res_qadr = ''
#    elif a == '' or b == '' or c == '':
#        my_discr = ''
#        res_qadr = ''
#    else:
#        my_discr = b*b - 4*a*c
#        if my_discr < 0:
#            res_qadr = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
#        elif my_discr == 0:
#            x1 = -b /(2 * a)
#            res_qadr = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x1)
#        elif my_discr > 0:
#            x1 = (-b + sqrt(my_discr)) / (2 * a)
#            x2 = (-b - sqrt(my_discr)) / (2 * a)
#            res_qadr = 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = '+ str(x2)

#        if my_discr != '':
#            my_discr = 'Дискриминант: ' + str(my_discr)

#    return render(request, 'results.html', {
#            'a': a,
#            'b': b,
#            'c': c,
#            'res_a': res_a,
#            'res_b': res_b,
#            'res_c': res_c,
#            'discr': my_discr,
#            'res_qadr': res_qadr
#})
