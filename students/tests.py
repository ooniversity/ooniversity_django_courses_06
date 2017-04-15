from django.test import TestCase, Client
from courses.models import Course
from students.models import Student

class StudentsListTest(TestCase):

    def test_students_list_200(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_students_nav_bar_have_contacts(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Contacts')

    def test_students_nav_bar_have_students(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Students')

    def test_students_nav_bar_have_feedback(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Feedback')

    def test_students_contains_brand(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Добавить нового студента')

class StudentsDetailTest(TestCase):

    def test_students_contain_name(self):
        client = Client()
        students = Student.objects.create(name='Zzz', surname='Xxx', phone='380672222222',)
        response = client.get('/students/1/')
        self.assertContains(response, 'Zzz')

    def test_students_contains_phone(self):
        client = Client()
        students = Student.objects.create(name='Zzz', surname='Xxx', phone='380672222222',)
        response = client.get('/students/1/')
        self.assertContains(response, '380672222222')

    def test_students_contains_date_of_birth(self):
        client = Client()
        students = Student.objects.create(name='Zzz', surname='Xxx', phone='380672222222',)
        response = client.get('/students/1/')
        self.assertContains(response, 'дата рождения')

    def test_students_contains_course(self):
        client = Client()
        students = Student.objects.create(name='Zzz', surname='Xxx', phone='380672222222',)
        response = client.get('/students/1/')
        self.assertContains(response, 'курсы')

    def test_students_contains_skype(self):
        client = Client()
        students = Student.objects.create(name='Zzz', surname='Xxx', phone='380672222222',)
        response = client.get('/students/1/')
        self.assertContains(response, 'логин skype')