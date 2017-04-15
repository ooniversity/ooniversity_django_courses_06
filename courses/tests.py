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

    def test_course_nav_bar_feedback(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'Feedback')

    def test_course_contains_brand(self):
        client = Client()
        response = client.get('/')
        self.assertContains(response, 'PyBursa')



class CoursesDetailTest(TestCase):

    def test_course_item_valid(self):
        client = Client()
        course = Course.objects.create(name='MyCourse', short_description='MyCourse short description', description='MyCourse full description')
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_item_error_404(self):
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_name(self):
        client = Client()
        course = Course.objects.create(name='MyCourse', short_description='MyCourse short description', description='MyCourse full description')
        response = client.get('/courses/1/')
        self.assertContains(response, 'MyCourse')

    def test_course_lesson_subject(self):
        client = Client()
        course = Course.objects.create(name='MyCourse', short_description='MyCourse short description', description='MyCourse full description')
        response = client.get('/courses/1/')
        lesson1 = Lesson.objects.create(subject = 'MyCourse lesson', description = 'MyCourse lesson description', course = course, order = '1')
        response = client.get('/courses/1/')
        self.assertContains(response, 'MyCourse lesson')

    def test_course_lesson_description(self):
        client = Client()
        course = Course.objects.create(name='MyCourse', short_description='MyCourse short description', description='MyCourse full description')
        lesson1 = Lesson.objects.create(subject = 'MyCourse lesson', description = 'MyCourse lesson description', course = course, order = '1')
        response = client.get('/courses/1/')
        self.assertContains(response, 'MyCourse lesson description')
