from django.test import TestCase
from courses.models import Course, Lesson

# Create your tests here.


class CoursesListTest(TestCase):

    def test_L_one(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
    
    def test_L_two(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                           short_description = 'ababagalamaga ababagalamaga ababagalamaga',
                                           )
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'kurs-1')
  

class CoursesDetailTest(TestCase):
    
    def test_D_one(self):
        pass