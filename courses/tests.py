from django.test import TestCase, Client
from courses.models import Course, Lesson

# Create your tests here.

class CoursesListTest(TestCase):
	
	def test_course_list_valid(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_course_nav_bar_main(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, 'Main')

	def test_course_nav_bar_contacts(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, 'Contacts')

	def test_course_nav_bar_students(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, 'Students')

	def test_course_nav_bar_quadratic_equation(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, 'Quadratic equation')

	def test_course_nav_bar_feedback(self):
		client = Client()
		response = client.get('/')
		self.assertContains(response, 'Feedback')


class CoursesDetailTest(TestCase):

	def test_course_item_valid(self):
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_course_item_error_404(self):
		client = Client()
		response = client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

	def test_course_name(self):
		client = Client()
		course = Course.objects.create(name='Course name', short_description='Short description',)
		response = client.get('/courses/1/')
		self.assertContains(response, 'Course name')

	def test_course_description(self):
		client = Client()
		course = Course.objects.create(name='Course name', short_description='Short description',)
		response = client.get('/courses/1/')
		self.assertContains(response, 'Course Plan')

	def test_course_add_lesson(self):
		client = Client()
		course = Course.objects.create(name='Course name', short_description='Short description',)
		response = client.get('/courses/1/')
		self.assertContains(response, 'href="/courses/1/add_lesson"')
