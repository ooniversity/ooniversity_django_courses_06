from django.test import TestCase
from courses.models import Course, Lesson

# Create your tests here.


class CoursesListTest(TestCase):

    def test_list_one(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)
    
    def test_list_two(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                           short_description = 'ababagalamaga ababagalamaga ababagalamaga',
                                           )
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'kurs-1')
  
    def test_list_three(self):
        pass

    def test_list_four(self):
        pass

    def test_list_five(self):
        pass

    def test_list_six(self):
        pass
    
    
class CoursesDetailTest(TestCase):
    
    def test_detail_one(self):
        pass

    def test_detail_two(self):
        pass


    def test_detail_three(self):
        pass


    def test_detail_four(self):
        pass


    def test_detail_five(self):
        pass


    def test_detail_six(self):
        pass
        