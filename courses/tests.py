from django.test import TestCase
from courses.models import Course
from django.test import Client

class StudentsListTest(TestCase):

    def test_courses_list(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_courses_list_create(self):
         first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
         self.assertEqual(Course.objects.all().count(), 1)

    def test_courses_list_delete(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        second_course = Course.objects.create( name="Course2", short_description = "Course2 desc", description = "Second course")
        third_course = Course.objects.create( name="Course3", short_description = "Course3 desc", description = "Third course")
        first_course.delete()
        self.assertEqual(Course.objects.all().count(), 2)

    def test_courses_list_update_without_name(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        first_course.short_description = 'Change short desc'
        first_course.description = 'Change description'
        first_course.save(update_fields=['description', 'short_description'])
        updated_object = Course.objects.get(name='Course1')
        self.assertEqual(updated_object.description, 'Change description')

    def test_courses_list__without_description(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        first_course.short_description = 'Change short desc'
        first_course.name = 'Change name'
        first_course.save(update_fields=['name', 'short_description'])
        updated_object = Course.objects.get(description='First course')
        self.assertEqual(updated_object.name, 'Change name')

class StudentsDetailTest(TestCase):
    
    def test_detail_get(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail_get_error(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        second_course = Course.objects.create( name="Course2", short_description = "Course2 desc", description = "Second course")
        client = Client()
        response = client.get('/courses/3/')
        self.assertEqual(response.status_code, 404)

    def test_detail_info_course_name(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        client = Client()
        response = client.get('/courses/1/')
        self.assertEqual(response.context['course'].name, 'Course1')

    def test_detail_info_page(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, "<title>Информация о курсе : Course1", status_code=200)

    def test_detail_info_page_update(self):
        first_course = Course.objects.create( name="Course1", short_description = "Course1 desc", description = "First course")
        first_course.short_description = 'Change short desc'
        first_course.description = 'Change description'
        first_course.name = 'Change name'
        first_course.save(update_fields=['description', 'short_description', 'name'])
        client = Client()
        response = client.get('/courses/1/')
        self.assertContains(response, "<title>Информация о курсе : Change name", status_code=200)