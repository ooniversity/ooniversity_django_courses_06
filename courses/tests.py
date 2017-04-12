from django.test import TestCase
from courses.models import Course

class CoursesListTest(TestCase):

    def test_course_list1(self):
        from django.test import Client
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_course_list2(self):
        course1 = Course.objects.create(name='Course_1',                                        short_description='Course_1 description')
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_list3(self):
        course1 = Course.objects.create(name='Course_1',
                                            short_description='Course_1 description')
        course2 = Course.objects.create(name='Course_2',
                                            short_description='Course_2 description')
        course3 = Course.objects.create(name='Course_3',
                                            short_description='Course_3 description')
        self.assertEqual(Course.objects.get(name='Course_1').name, 'Course_1')

    def test_course_list4(self):
        course1 = Course.objects.create(name='Course_1',
                                            short_description='Course_1 description')
        course2 = Course.objects.create(name='Course_2',
                                            short_description='Course_2 description')
        course3 = Course.objects.create(name='Course_3',
                                            short_description='Course_3 description')
        self.assertEqual(Course.objects.get(short_description='Course_2 description').short_description,
                                                   'Course_2 description')

    def test_course_list5(self):
        course1 = Course.objects.create(name='Course_1',
                                                short_description='Course_1 description')
        course2 = Course.objects.create(name='Course_2',
                                                short_description='Course_2 description')
        course3 = Course.objects.create(name='Course_3',
                                                short_description='Course_3 description')
        Course.objects.get(name='Course_1').delete()
        self.assertEqual(Course.objects.all().count(), 2)


class CoursesDetailTest(TestCase):
    def test_course_detail1(self):
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

    def test_course_detail2(self):
        course1 = Course.objects.create(name='Course_1',
                                        short_description='Course_1 description')
        from django.test import Client
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)

    def test_course_detail3(self):
        course1 = Course.objects.create(name='Course_1',
                                            short_description='Course_1 description')
        course2 = Course.objects.create(name='Course_2',
                                            short_description='Course_2 description')
        course3 = Course.objects.create(name='Course_3',
                                            short_description='Course_3 description')
        from django.test import Client
        client = Client()
        response = client.get('/courses/3/')
        self.assertEqual(response.context['course'].name, 'Course_3')

    def test_course_detail4(self):
        course1 = Course.objects.create(name='Course_1',
                                            short_description='Course_1 description')
        course2 = Course.objects.create(name='Course_2',
                                            short_description='Course_2 description')
        course3 = Course.objects.create(name='Course_3',
                                            short_description='Course_3 description')
        from django.test import Client
        client = Client()
        response = client.get('/courses/3/')
        self.assertEqual(response.context['title'], 'Course creation')

    def test_course_detail5(self):
        course1 = Course.objects.create(name='Course_1',
                                            short_description='Course_1 description')
        course2 = Course.objects.create(name='Course_2',
                                            short_description='Course_2 description')
        course3 = Course.objects.create(name='Course_3',
                                            short_description='Course_3 description')
        from django.test import Client
        client = Client()
        response = client.get('/courses/3/')
        self.assertEqual(response.context['course'].short_description, 'Course_3 description')
