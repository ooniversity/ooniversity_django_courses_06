'''
    Test cases module for courses application
'''

from django.test import TestCase
from django.test import Client

from courses.models import Course, Lesson


class CoursesListTest(TestCase):
    '''
        Test cases class for courses list
    '''

    def test_courses_page(self):
        '''
            Check that page with courses list (index page) exist.
        '''

        client = Client()

        response = client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_courses_name(self):
        '''
            Check that courses names are in upper case on the page.
        '''

        client = Client()

        course_name = 'New test course'

        Course.objects.create(
            name=course_name,
            short_description='Test course test description',
        )

        response = client.get('/')

        self.assertContains(response, course_name.upper())

    def test_courses_short_description(self):
        '''
            Check that courses short description are in capitalize on the page.
        '''

        client = Client()

        course_description = 'Test course test description'

        Course.objects.create(
            name='New test course',
            short_description=course_description
        )

        response = client.get('/')

        self.assertContains(response, course_description.title())

    def test_courses_edit_button(self):
        '''
            Check that there is correct course edit button on the page.
        '''

        client = Client()

        Course.objects.create(
            name='New test course',
            short_description='Test course test description'
        )

        response = client.get('/')

        self.assertContains(response, 'href="/courses/edit/1/"')

    def test_courses_remove_button(self):
        '''
            Check that there is correct course remove button on the page.
        '''

        client = Client()

        Course.objects.create(
            name='New test course',
            short_description='Test course test description'
        )

        response = client.get('/')

        self.assertContains(response, 'href="/courses/remove/1/"')


class CoursesDetailTest(TestCase):
    '''
        Test cases class for course detail page
    '''

    def test_detail_page(self):
        '''
            Check that single page with course can be created.
        '''

        client = Client()

        response = client.get('/courses/1/')

        self.assertEqual(response.status_code, 404)

        Course.objects.create(
            name='New Test Course',
            description='Test course test description',
        )

        response = client.get('/courses/1/')

        self.assertEqual(response.status_code, 200)

    def test_course_name(self):
        '''
            Check that course name are in the page.
        '''

        client = Client()

        course_name = 'New test course'

        Course.objects.create(
            name=course_name,
            description='Test course test description',
        )

        response = client.get('/courses/1/')

        self.assertContains(response, course_name)

    def test_course_description(self):
        '''
            Check that course description truncated to 32 characters.
        '''

        client = Client()

        course_description = ('New test course provide a basic understanding'
                              'of the Python language.')

        Course.objects.create(
            name='New test course',
            description=course_description,
        )

        response = client.get('/courses/1/')

        self.assertContains(response, '{}...'.format(course_description[:29]))

    def test_lesson(self):
        '''
            Check that lesson can be created and it contain needed information
        '''

        client = Client()

        course = Course.objects.create(
            name='New Test Course',
            short_description='Test course test description',
        )

        Lesson.objects.create(
            subject='Test lesson',
            description='Test lesson description',
            course=course,
            order=1
        )

        response = client.get('/courses/1/')

        self.assertEqual(Lesson.objects.all().count(), 1)
        self.assertContains(response, 'Test lesson')

    def test_lesson_add_button(self):
        '''
            Check that page contain Add new course button.
        '''

        client = Client()

        Course.objects.create(
            name='New test course',
            short_description='Test course test description'
        )

        response = client.get('/courses/1/')

        self.assertContains(response, 'href="/courses/1/add_lesson/"')
