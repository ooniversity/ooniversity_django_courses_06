from django.test import TestCase, Client
from courses.models import Course
from students.models import Student

class StudentsListTest(TestCase):

    def test_students_list_valid(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_students_nav_bar_main(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Main')

    def test_students_nav_bar_contacts(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Contacts')

    def test_students_nav_bar_students(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Students')

    def test_students_nav_bar_quadratic_equation(self):
        client = Client()
        response = client.get('/students/')
        self.assertContains(response, 'Quadratic Equation')

    def test_students_nav_bar_feedback(self):
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
        students = Student.objects.create(name='Ivan',
                                          surname='Ivanov',
                                          phone='096XXXXXXXX',
                                          )
        response = client.get('/students/1/')
        self.assertContains(response, 'Ivan')

    def test_students_contains_brand(self):
        client = Client()
        students = Student.objects.create(name='Ivan',
                                          surname='Ivanov',
                                          phone='096XXXXXXXX',
                                          )
        response = client.get('/students/1/')
        self.assertContains(response, 'Детали о студенте')

    def test_students_contains_date_of_birth(self):
        client = Client()
        students = Student.objects.create(name='Ivan',
                                          surname='Ivanov',
                                          phone='096XXXXXXXX',
                                          )
        response = client.get('/students/1/')
        self.assertContains(response, 'дата рождения')

    def test_students_contains_date_of_course(self):
        client = Client()
        students = Student.objects.create(name='Ivan',
                                          surname='Ivanov',
                                          phone='096XXXXXXXX',
                                          )
        response = client.get('/students/1/')
        self.assertContains(response, 'курсы')

    def test_students_contains_date_of_course(self):
        client = Client()
        students = Student.objects.create(name='Ivan',
                                          surname='Ivanov',
                                          phone='096XXXXXXXX',
                                          )
        response = client.get('/students/1/')
        self.assertContains(response, 'курсы')

    def test_students_detail_nav_bar_feedback(self):
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, 'Students')