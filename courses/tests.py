# -*- coding: utf-8 -*-
from django.test import TestCase
from courses.models import Course, Lesson
from coaches.models import Coach
from django.contrib.auth.models import User


# Create your tests here.
class CoursesListTest(TestCase):


	def test_courses_page(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')


	def test_cource_create(self):
		course = Course.objects.create(
							name = 'PyBursa2',
							short_description="Web development with django")
		self.assertEqual(Course.objects.all().count(),1)


	def test_cource_valid(self):
		course = Course.objects.create(
							name = 'PyBursa2',
							short_description="Web development with django")

		response = self.client.get('/')
		self.assertEqual(response.context['courses'][0].name, course.name)
		self.assertEqual(response.context['courses'][0].short_description, course.short_description)

	def test_course_valid_add(self):
		response = self.client.get('/courses/add/')
		self.assertContains(response, 'Name')
		self.assertContains(response, 'Short description')
		self.assertContains(response, 'Description')
		self.assertContains(response, 'Coach')
		self.assertContains(response, 'Assistant')

	def test_course_link_present(self):
		course = Course.objects.create(
							name = 'PyBursa2',
							short_description='Web development with django')

		response = self.client.get('/')
		self.assertContains(response, '/courses/add/')
		self.assertContains(response, '/courses/edit/1/')
		self.assertContains(response, '/courses/remove/1/')


class CoursesDetailTest(TestCase):

	def test_course_detail_404(self):
		response = self.client.get('/courses/1/')
		self.assertEqual(response.status_code, 404)

	def test_add_lesson(self):

		course = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
		)

		lesson1 = Lesson.objects.create(subject='Введение Python', order=1, course=course)
		lesson2 = Lesson.objects.create(subject='Основы Python', order=2, course=course)
		response = self.client.get('/courses/1/')
		self.assertEqual(Lesson.objects.all().count(),2)

	def test_coache_datail_page(self):
		user = User.objects.create(username='User1')

		course = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
		)

		coach = Coach.objects.create(
			user=user,
			date_of_birth='1988-01-01'
		)

		response = self.client.get('/coaches/1/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'coaches/detail.html')

	def test_cource_lesson_subject(self):

		course = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
		)

		lesson1 = Lesson.objects.create(subject='Введение Python', order=1, course=course)
		lesson2 = Lesson.objects.create(subject='Основы Python', order=2, course=course)
		response = self.client.get('/courses/1/')
		for lesson in course.lesson_set.all():
			self.assertContains(response, lesson.subject)

	def test_coache_valid(self):

		user = User.objects.create(
			username='User',
			first_name="Zarina"
		)

		coach = Coach.objects.create(
			user=user,
			date_of_birth='1988-01-01',
			description='Zarina description'
		)
		course = Course.objects.create(
			name='PyBursa2',
			short_description='Web development with django',
			coach = coach,
			assistant=coach
		)

		response = self.client.get('/courses/1/')
		self.assertContains(response, user.first_name)
		self.assertContains(response, coach.description)
