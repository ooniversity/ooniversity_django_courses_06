from django.test import TestCase
from courses.models import Course

class CoursesListTest(TestCase):

    def test_list_page(self):
        from django.test import Client

        client = Client()

        Course.objects.create(
            name='New Test Course',
            short_description='Test course test description',
        )

        response = client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'NEW TEST COURSE')


class CoursesDetailTest(TestCase):

    def test_detail_page(self):
        from django.test import Client

        client = Client()

        response = client.get('/courses/1/')

        self.assertEqual(response.status_code, 404)

        Course.objects.create(
            name='New Test Course',
            short_description='Test course test description',
        )

        response = client.get('/courses/1/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'New Test Course')
