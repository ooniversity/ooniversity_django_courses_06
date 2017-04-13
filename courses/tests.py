from django.test import TestCase, Client
from courses.models import Course, Lesson


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
        self.assertContains(response, 'Quadratic Equation')

    def test_course_nav_bar_feedback(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Feedback')

    def test_course_contains_brand(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'ItBursa')



class CoursesDetailTest(TestCase):

    def test_course_item_valid(self):
        client = Client()
        course = Course.objects.create(name='Some Course',
                                       short_description='Short description',
                                       description='Default',
                                       )
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_item_error_404(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_lesson_name(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Course short description',
                                       description='Course description',
                                       )
        response = client.get('/courses/1/')
        self.assertContains(response, 'Course name')

    def test_course_lesson_description(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Course short description',
                                       description='Course description',
                                       )
        response = client.get('/courses/1/')
        self.assertContains(response, 'Course description')

        lesson1 = Lesson.objects.create(subject = 'Lesson subject',
                                        description = 'Lesson description',
                                        course = course,
                                        order = '1'
                                        )

        response = client.get('/courses/1/')
        self.assertContains(response, 'Lesson subject')

    def test_course_lesson_subject(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Course short description',
                                       description='Course description',
                                       )
        lesson = Lesson.objects.create(subject='Name of Lesson',
                                       description='Description of Lesson',
                                       course=course,
                                       order='1',
                                       )

        response = self.client.get('/courses/1/')

    def test_course_add_lesson(self):
        client = Client()
        course = Course.objects.create(name='Test Course', 
                                       short_description='Web tests course'
                                       )
        response = self.client.get('/courses/1/')
        self.assertContains(response, 'Добавить занятие')
