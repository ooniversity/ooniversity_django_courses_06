from django.test import TestCase
from students.models import Student

class StudentsListTest(TestCase):

    def test_student_create(self):

        Student.objects.create(
            name='Test student',
            surname='testich',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='alskj alskjf',
            skype='skype'
        )

        self.assertEqual(Student.objects.all().count(), 1)


    def test_list_page(self):
        from django.test import Client

        client = Client()

        Student.objects.create(
            name='Abracadabra',
            surname='testich',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='alskj alskjf',
            skype='skype'
        )

        response = client.get('/students/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Abracadabra')


class StudentsDetailTest(TestCase):

    def test_detail_page(self):
        from django.test import Client

        client = Client()

        response = client.get('/students/1/')

        self.assertEqual(response.status_code, 404)

        Student.objects.create(
            name='Abracadabra',
            surname='testich',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='alskj alskjf',
            skype='skype'
        )

        response = client.get('/students/1/')

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Abracadabra')
