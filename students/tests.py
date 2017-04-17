'''
    Test cases module for students application
'''

from django.test import TestCase
from django.test import Client

from students.models import Student


class StudentsListTest(TestCase):
    '''
        Test cases class for students list
    '''

    def test_student_create(self):
        '''
            Check that student can be breated
        '''

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        self.assertEqual(Student.objects.all().count(), 1)

    def test_list_page(self):
        '''
            Check that students page exist.
        '''

        client = Client()

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/')

        self.assertEqual(response.status_code, 200)

    def test_students_name(self):
        '''
            Check that students names and surnames are capitalize on the page.
        '''

        client = Client()

        student_name = 'john'
        student_surname = 'doe'

        Student.objects.create(
            name=student_name,
            surname=student_surname,
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/')

        self.assertContains(response, student_name.title())
        self.assertContains(response, student_surname.title())

    def test_student_add_button(self):
        '''
            Check that page contain 'Add new student' button.
        '''

        client = Client()

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/')

        self.assertContains(response, 'href="/students/add/"')

    def test_student_edit_button(self):
        '''
            Check that page contain correct student edit button.
        '''

        client = Client()

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/')

        self.assertContains(response, 'href="/students/edit/1/"')

    def test_student_remove_button(self):
        '''
            Check that page contain correct student remove button.
        '''

        client = Client()

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/')

        self.assertContains(response, 'href="/students/remove/1/"')


class StudentsDetailTest(TestCase):
    '''
        Test cases class for student detail page
    '''

    def test_detail_page(self):
        '''
            Check that single student page can be created.
        '''

        client = Client()

        response = client.get('/students/1/')

        self.assertEqual(response.status_code, 404)

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/1/')

        self.assertEqual(response.status_code, 200)

    def test_student_name(self):
        '''
            Check that student name is capitalize on the page.
        '''

        client = Client()

        student_name = 'john john'

        Student.objects.create(
            name=student_name,
            surname='doe',
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/1/')

        self.assertContains(response, student_name.title())

    def test_student_surname(self):
        '''
            Check that student surname is capitalize on the page.
        '''

        client = Client()

        student_surname = 'doe doe'

        Student.objects.create(
            name='john',
            surname=student_surname,
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/1/')

        self.assertContains(response, student_surname.title())

    def test_student_birth(self):
        '''
            Check that student birth date has format like '31 December, 2016'
        '''

        client = Client()

        date_of_birth = '2016-12-31'

        Student.objects.create(
            name='john',
            surname='doe',
            date_of_birth=date_of_birth,
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/1/')

        self.assertContains(response, '31 December, 2016')

    def test_student_name_surname_title(self):
        '''
            Check that student name and surname is in the page title.
        '''

        client = Client()

        student_name = 'john'
        student_surname = 'doe'

        Student.objects.create(
            name=student_name,
            surname=student_surname,
            date_of_birth='1910-01-23',
            email='test_stud@example.com',
            phone='1234',
            address='some address',
            skype='skype'
        )

        response = client.get('/students/1/')

        self.assertContains(response,
                            '<title>{} {}'
                            .format(student_name, student_surname))
