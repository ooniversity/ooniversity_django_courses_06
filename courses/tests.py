from django.test import TestCase
from courses.models import Course, Lesson

# Create your tests here.


class CoursesListTest(TestCase):

    def test_list_one(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    
    def test_list_two(self):
        response = self.client.get('/')
        self.assertContains(response, 'Вітаємо сайті')
  
    def test_list_three(self):
        response = self.client.get('/')
        self.assertContains(response, 'ПЕРЕЛІК КУРСІВ')

    def test_list_four(self):
        response = self.client.get('/')
        self.assertContains(response, 'href="/courses/add/"')

    def test_list_five(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                            short_description = 'ababagalamaga',                                           )
        response = self.client.get('/')
        self.assertContains(response, 'href="/courses/edit/1/"')

    def test_list_six(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                            short_description = 'ababagalamaga',                                           )
        response = self.client.get('/')
        self.assertContains(response, 'href="/courses/remove/1/"')
    
    
class CoursesDetailTest(TestCase):
    
    def test_detail_one(self):
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)


    def test_detail_two(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                            short_description = 'ababagalamaga',
                                            )
        response = self.client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'kurs-1')


    def test_detail_three(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                            short_description = 'ababagalamaga',
                                            )
        response = self.client.get('/courses/1/')
        self.assertContains(response,'href="/courses/1/add_lesson"')        

    def test_detail_four(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                            short_description = 'ababagalamaga',
                                            )
        response = self.client.get('/courses/1/add_lesson')
        self.assertContains(response,'kurs-1')        


    def test_detail_five(self):
        add_course1 = Course.objects.create(name = 'kurs-1',
                                            short_description = 'ababagalamaga',
                                            )
        add_lesson1 = Lesson.objects.create(subject = 'UROK KUROK',
                                            description = 'opis uroku',
                                            course = add_course1,
                                            order = '1',)
        response = self.client.get('/courses/1/')
        self.assertContains(response,'opis uroku')
        

