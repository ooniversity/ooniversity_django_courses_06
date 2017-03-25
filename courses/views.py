from django.shortcuts import render
from courses.models import Course, Lesson

def detail(request, course_id):
	course = Course.objects.get(id=course_id)
	lessons_list = Lesson.object.filter(course=course)

	context = {
		'course': course,
		'lessons_list': lessons_list
	}
	
	return render(request, 'courses/detail.html', context)
