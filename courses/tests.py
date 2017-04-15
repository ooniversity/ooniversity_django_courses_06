from django.test import TestCase
from django.test import Client
from courses.models import Course, Lesson
# Create your tests here.


class CoursesListTest(TestCase):
    
    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_courses1(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        response = client.get('/')
        self.assertContains(response, 'COURSE NAME')

    def test_courses2(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        response = client.get('/')
        self.assertContains(response, 'Description')

    def test_courses3(self):
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                        )
        self.assertEqual(Course.objects.all().count(), 1)
    
    def test_index_list(self):
        client = Client()
        response = self.client.get('/')
        self.assertContains(response, 'PyBursa')


class CoursesDetailTest(TestCase):
    def test_course_presented(self):
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        self.assertEqual(Course.objects.all().count(), 1)

    def test_course_detail1(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
    
    
    def test_course_detail2(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        response = client.get('/courses/1/')    
        self.assertContains(response, 'Course name')    

    def test_course_detail3(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        response = client.get('/courses/1/')    
        self.assertContains(response, 'Description')  

    def test_course_detail4(self):
        client = Client()
        course = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        response = client.get('/courses/1/')    
        self.assertContains(response, 'Add lesson')  
        


    def test_course_detail5(self):
        client = Client()
        course1 = Course.objects.create(name='Course name',
                                       short_description='Short descr',
                                       description='Description',
                                       )
        lesson = Lesson.objects.create(subject='Subject name',
                                        description='Lesson description',
                                        course = course1,
                                        order='1',
                                        )
        response = client.get('/courses/1/')    
        self.assertContains(response, 'Subject name')
    
