from django.test import TestCase
from django.test import Client
from courses.models import Course, Lesson
from students.models import Student
from django.core.paginator import Paginator
# Create your tests here.

class StudentsListTest(TestCase):
    def test_student_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
    
    def test_studednt1(self):
        client = Client()
        student = Student.objects.create(name='Name',
                                       surname='Surname',
                                       phone='144443',
                                       address='Address',
                                       skype='skypename',
                                       email='email@mail.com',
                                       )
        response = client.get('/students/')
        self.assertContains(response, 'Name')
        self.assertContains(response, 'skypename')
        self.assertContains(response, 'Edit student')

    def test_student_list(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertContains(response, 'Address')

    def test_student_list_button1(self):
        client = Client()
        response = self.client.get('/students/')
        self.assertContains(response, 'Add student')
    
    def test_student_created(self):
        student = Student.objects.create(name='Name',
                                       surname='Surname',
                                       phone='144443',
                                       address='Address',
                                       skype='skypename',
                                       email='email@mail.com',
                                       )
        self.assertEqual(Student.objects.all().count(), 1)
    



class StudentsDetailTest(TestCase):
    def test_student_creted(self):
        student = Student.objects.create(name='Name',
                                       surname='Surname',
                                       phone='144443',
                                       address='Address',
                                       skype='skypename',
                                       email='email@mail.com',
                                       )
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student1(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

    def test_student2(self):
        client = Client()
        student = Student.objects.create(name='Name',
                                       surname='Surname',
                                       phone='144443',
                                       address='Address',
                                       skype='skypename',
                                       email='email@mail.com',
                                       )
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student3(self):
        client = Client()
        student = Student.objects.create(name='Name',
                                       surname='Surname',
                                       phone='144443',
                                       address='Address',
                                       skype='skypename',
                                       email='email@mail.com',
                                       )
        response = client.get('/students/1/')
        self.assertContains(response, 'Name')
    
    def test_student4(self):
        client = Client()
        student = Student.objects.create(name='Name',
                                       surname='Surname',
                                       phone='144443',
                                       address='Address',
                                       skype='skypename',
                                       email='email@mail.com',
                                       )
        response = client.get('/students/1/')
        self.assertContains(response, 'email@mail.com')
    
    
