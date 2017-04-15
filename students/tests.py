from django.test import TestCase
from students.models import Student
from courses.models import Course


# Create your tests here.
class StudentsListTest(TestCase):

    def test_list_one(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_list_two(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'TechBursa Python/Django 06 :: Students - list')

    def test_list_three(self):
        response = self.client.get('/students/')
        self.assertContains(response, 'href="/students/add/"')
      
    def test_list_four(self):
        new_course = Course.objects.create(name = 'kurs-1',
                              short_description = 'ababagalamaga',
                              )
        for item in range(1,5):
            new_student = Student.objects.create(name='Student'+str(item),
                                                 surname='Surname'+str(item),
                                                 )
            new_student.save()
            new_student.courses.add(new_course)
        
        response = self.client.get('/students/?course_id=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'next >>')

    def test_list_five(self):
        new_student = Student.objects.create(name='ABABA',
                                             surname='GALAMAGA',
                                             )
        new_student.courses.create(name='ZULU ALERT',
                                   short_description='BANZAI',)
        response = self.client.get('/students/')
        self.assertContains(response, 'Удалить')
        self.assertContains(response, 'GALAMAGA ABABA')

    def test_list_six(self):
        new_student = Student.objects.create(name='Aaaaaaaaaaa',
                                             surname='Bbbbbbbb',
                                             skype='aaa_bbb',
                                             )
        response = self.client.get('/students/')
        self.assertContains(response, 'href="/students/edit/1/"')
        self.assertContains(response, 'aaa_bbb')

class StudentsDetailTest(TestCase):

    def test_detail_one(self):
        response = self.client.get('/students/1/')
        self.assertEqual(response.status_code, 404)


    def test_detail_two(self):
        new_student = Student.objects.create(name='XXX',
                                             surname='YYY',
                                             )
        response = self.client.get('/students/1/')
        self.assertContains(response, 'XXX YYY')


    def test_detail_three(self):
        new_student = Student.objects.create(name='XXX',
                                             surname='YYY',
                                             date_of_birth = '1971-01-01'
                                             )
        response = self.client.get('/students/1/')
        self.assertContains(response, 'Jan. 01, 1971')


    def test_detail_four(self):
        new_student = Student.objects.create(name='XXX',
                                             surname='YYY',
                                             )
        response = self.client.get('/students/1/')
        self.assertContains(response, 'XXX YYY')


    def test_detail_five(self):
        new_student = Student.objects.create(name='XXX',
                                             surname='YYY',
                                             )
        response = self.client.get('/students/1/')
        self.assertContains(response, '<a href="/students/?course_id=">Students</a>')


    def test_detail_six(self):
        new_course = Course.objects.create(name = 'KURS BONSAI',
                              short_description = 'JAPANISE CULTURE',
                              )
        new_student = Student.objects.create(name='XXX',
                                             surname='YYY',
                                             )
        new_student.courses.add(new_course)
        
        response = self.client.get('/students/1/')
        self.assertContains(response, 'BONSAI')
    