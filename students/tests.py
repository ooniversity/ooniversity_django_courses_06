from django.test import TestCase, Client
from courses.models import Course
from students.models import Student

# Create your tests here.

class StudentsListTest(TestCase):
	
	def test_students_list_valid(self):
		client = Client()
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

	def test_students_nav_bar_main(self):
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, 'Main')

	def test_students_nav_bar_contacts(self):
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, 'Contacts')

	def test_students_nav_bar_students(self):
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, 'Students')

	def test_students_nav_bar_quadratic_equation(self):
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, 'Quadratic equation')

	def test_students_nav_bar_feedback(self):
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, 'Feedback')


class StudentsDetailTest(TestCase):

	def test_students_contain_name(self):
		client = Client()
		students = Student.objects.create(name='Oleksandr', surname='Holtzer', phone='911',)
		response = client.get('/students/1/')
		self.assertContains(response, 'Oleksandr')

	def test_students_contain_surname(self):
		client = Client()
		students = Student.objects.create(name='Oleksandr', surname='Holtzer', phone='911',)
		response = client.get('/students/1/')
		self.assertContains(response, 'Holtzer')

	def test_students_contain_phone(self):
		client = Client()
		students = Student.objects.create(name='Oleksandr', surname='Holtzer', phone='911',)
		response = client.get('/students/1/')
		self.assertContains(response, '911')

	def test_students_contain_date_of_birth(self):
		client = Client()
		students = Student.objects.create(name='Oleksandr', surname='Holtzer', date_of_birth='2012-01-01',)
		response = client.get('/students/1/')
		self.assertContains(response, 'Jan. 1, 2012')

	def test_students_contain_skype(self):
		client = Client()
		students = Student.objects.create(name='Oleksandr', surname='Holtzer', skype='oleks_holtzer',)
		response = client.get('/students/1/')
		self.assertContains(response, 'oleks_holtzer')
