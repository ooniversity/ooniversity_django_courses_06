from django.test import TestCase
from courses.models import Course

class CourseTests(TestCase):
    
    def test_course_create(self):
        course1 = Course.objects.create(
                           name='PyBursa06',
                           short_description="Web development with django")
        self.assertEqual(Course.objects.all().count(), 1)
