from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach

def detail(request, course_id):
	course = Course.objects.get(id=course_id)
	lessons_list = Lesson.objects.filter(course=course_id)
	coach = Coach.objects.get(id=course.coach.id)
	assistant = Coach.objects.get(id=course.assistant.id)
	
	return render(request, 'courses/detail.html', {'course':course, 'lessons_list':lessons_list, 'coach':coach, 'assistant':assistant})
