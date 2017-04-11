from django.test import TestCase
from students.models import Student

class StudentsListTest(TestCase):

    def test_student1(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student2(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student3(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        student2 = Student.objects.create(name='Student_2_name', surname='Student_2_surname', date_of_birth='1917-01-02',
                                        email='student2@email.com', phone='2222222', address='student2_address',
                                        skype='student2_skype')
        student3 = Student.objects.create(name='Student_3_name', surname='Student_3_surname', date_of_birth='1917-01-03',
                                        email='student3@email.com', phone='3333333', address='student3_address',
                                        skype='student3_skype')

        self.assertEqual(Student.objects.get(name='Student_1_name').name, 'Student_1_name')

    def test_student4(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        student2 = Student.objects.create(name='Student_2_name', surname='Student_2_surname', date_of_birth='1917-01-02',
                                        email='student2@email.com', phone='2222222', address='student2_address',
                                        skype='student2_skype')
        student3 = Student.objects.create(name='Student_3_name', surname='Student_3_surname', date_of_birth='1917-01-03',
                                        email='student3@email.com', phone='3333333', address='student3_address',
                                        skype='student3_skype')

        self.assertEqual(Student.objects.get(skype='student1_skype').skype,
                                                   'student1_skype')

    def test_student5(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        student2 = Student.objects.create(name='Student_2_name', surname='Student_2_surname', date_of_birth='1917-01-02',
                                        email='student2@email.com', phone='2222222', address='student2_address',
                                        skype='student2_skype')
        student3 = Student.objects.create(name='Student_3_name', surname='Student_3_surname', date_of_birth='1917-01-03',
                                        email='student3@email.com', phone='3333333', address='student3_address',
                                        skype='student3_skype')

        Student.objects.get(name='Student_1_name').delete()

        self.assertEqual(Student.objects.all().count(), 2)


class StudentsDetailTest(TestCase):
    def test_student_detail1(self):
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

    def test_student_detail2(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        from django.test import Client
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_student_detail3(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        student2 = Student.objects.create(name='Student_2_name', surname='Student_2_surname', date_of_birth='1917-01-02',
                                        email='student2@email.com', phone='2222222', address='student2_address',
                                        skype='student2_skype')
        student3 = Student.objects.create(name='Student_3_name', surname='Student_3_surname', date_of_birth='1917-01-03',
                                        email='student3@email.com', phone='3333333', address='student3_address',
                                        skype='student3_skype')
        from django.test import Client
        client = Client()
        response = client.get('/students/3/')
        self.assertEqual(response.context['student'].name, 'Student_3_name')

    def test_student_detail4(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        student2 = Student.objects.create(name='Student_2_name', surname='Student_2_surname', date_of_birth='1917-01-02',
                                        email='student2@email.com', phone='2222222', address='student2_address',
                                        skype='student2_skype')
        student3 = Student.objects.create(name='Student_3_name', surname='Student_3_surname', date_of_birth='1917-01-03',
                                        email='student3@email.com', phone='3333333', address='student3_address',
                                        skype='student3_skype')
        from django.test import Client
        client = Client()
        response = client.get('/students/3/')
        self.assertEqual(response.context['student'].surname, 'Student_3_surname')

    def test_student_detail5(self):
        student1 = Student.objects.create(name='Student_1_name', surname='Student_1_surname', date_of_birth='1917-01-01',
                                        email='student1@email.com', phone='111111', address='student1_address',
                                        skype='student1_skype')
        student2 = Student.objects.create(name='Student_2_name', surname='Student_2_surname', date_of_birth='1917-01-02',
                                        email='student2@email.com', phone='2222222', address='student2_address',
                                        skype='student2_skype')
        student3 = Student.objects.create(name='Student_3_name', surname='Student_3_surname', date_of_birth='1917-01-03',
                                        email='student3@email.com', phone='3333333', address='student3_address',
                                        skype='student3_skype')
        from django.test import Client
        client = Client()
        response = client.get('/students/3/')
        self.assertEqual(response.context['student'].email, 'student3@email.com')