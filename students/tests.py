from django.test import TestCase
from students.models import Student
from django.test import Client

class StudentsListTest(TestCase):

    def test_students_list(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_students_list_create(self):
         first_student = Student.objects.create( name="Student1", phone = "555", email = "a@a.com")
         self.assertEqual(Student.objects.all().count(), 1)

    def test_students_list_delete(self):
        first_student = Student.objects.create( name="Student1", phone = "555", email = "a@a.com")
        second_student = Student.objects.create( name="Student2", phone = "7777", email = "b@m.com")
        third_student = Student.objects.create( name="Student3", phone = "7777", email = "c@c.com")
        first_student.delete()
        self.assertEqual(Student.objects.all().count(), 2)

    def test_students_list_update_without_name(self):
        first_student = Student.objects.create( name="Student1", phone = "555", email = "a@a.com")
        first_student.phone = '11111'
        first_student.email = 'update_a@a.com'
        first_student.name = 'Update name'
        first_student.save(update_fields=['phone', 'email'])
        updated_object = Student.objects.get(name='Student1')
        self.assertEqual(updated_object.email, 'update_a@a.com')

    def test_students_list__without_description(self):
        first_student = Student.objects.create( name="Student1", phone = "555", email = "a@a.com")
        first_student.phone = '11111'
        first_student.email = 'update_a@a.com'
        first_student.name = 'Change name'
        first_student.save(update_fields=['name', 'phone', 'email'])
        updated_object = Student.objects.get(email='update_a@a.com')
        self.assertEqual(updated_object.phone, '11111')

class StudentsDetailTest(TestCase):
    
    def test_detail_get(self):
        client = Client()
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_detail_get_error(self):
        first_student = Student.objects.create( name="Student1", phone = "555", email = "a@a.com")
        second_student = Student.objects.create( name="Student2", phone = "7777", email = "b@m.com")
        client = Client()
        response = client.get('/students/5/')
        self.assertEqual(response.status_code, 404)

    def test_detail_info_student_name(self):
        first_student = Student.objects.create( name="Student1", phone = "555", email = "a@a.com")
        client = Client()
        response = client.get('/students/1/')
        self.assertEqual(response.context['student'].phone, '555')

    def test_detail_info_page(self):
        first_student = Student.objects.create( name="Student1", surname = 'Student1', phone = "555", email = "a@a.com")
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, "<title> Данные скубента : Student1 Student1", status_code=200)

    def test_detail_info_page_update(self):
        first_student = Student.objects.create( name="Student1", surname = 'Student1',phone = "555", email = "a@a.com")
        first_student.phone = '888888888888'
        first_student.email = 'update_a@a.com'
        first_student.name = 'Change name'
        first_student.save(update_fields=['phone', 'email', 'name'])
        client = Client()
        response = client.get('/students/1/')
        self.assertContains(response, "<title> Данные скубента : Change name Student1", status_code=200)