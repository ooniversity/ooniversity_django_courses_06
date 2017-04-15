# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from students.models import Student
from courses.models import Course
from django.test import Client
from django.core.urlresolvers import reverse

# Create your tests here.
class StudentsListTest(TestCase):

	def test_student_page_status(self):
		response = self.client.get('/students/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'students/student_list.html')

	def test_student_create(self):
		for i in xrange(10):
			student = Student.objects.create(
								name='Chuck{}'.format(i+1),
								surname='Norris{}.format(i+1)',
								date_of_birth=datetime.date(1988, 02, 02),)

		response = self.client.get('/students/')
		self.assertEqual(Student.objects.all().count(), 10)

	def test_student_context(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		response = self.client.get('/students/')
		self.assertEqual(response.context['student_list'][0],
                         student)

	def test_student_valid(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')
		response = self.client.get('/students/')
		self.assertContains(response, student.surname)
		self.assertContains(response, student.name)

	def test_student_link_check(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		response = self.client.get('/students/')
		self.assertContains(response, '/students/add/')
		self.assertContains(response, '/students/1/')
		self.assertContains(response, '/students/edit/1/')
		self.assertContains(response, '/students/remove/1/')


class StudentsDetailTest(TestCase):

	def test_student_detail_404(self):
		response = self.client.get('/students/1/')
		self.assertEqual(response.status_code, 404)

	def test_student_add_to_course(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		course1 = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
		)
		course2 = Course.objects.create(
			name='JSBursa2',
			short_description='Web development with JavaScript',
		)
		student.courses.add(course1)
		student.courses.add(course2)

		client = Client()
		response = client.get(reverse('students:detail', args=(1,)))

		for course	in student.courses.all():
			self.assertContains(response, course.name)

	def test_student_detail_view(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		client = Client()
		response = client.get(reverse('students:detail', args=(1,)))
		self.assertEqual(response.status_code, 200)

	def test_get_template(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		response = self.client.get('/students/1/')
		self.assertTemplateUsed(response, 'students/student_detail.html')


	def test_student_add_to_course(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		course1 = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
		)
		course2 = Course.objects.create(
			name='JSBursa2',
			short_description='Web development with JavaScript',
		)

		student.courses.add(course1)
		student.courses.add(course2)
		student_courses=student.courses.all()
		self.assertEqual(student_courses.count(), 2)

	def test_student_check_course(self):
		student = Student.objects.create(
			name='Test',
			surname='Test',
			date_of_birth='1988-02-02')

		course1 = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
		)
		student.courses.add(course1)
		response = self.client.get('/students/1/')
		self.assertContains(response, 'PyBursa2')
		self.assertContains(response, '/courses/1/')
