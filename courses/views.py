from django.shortcuts import render
from courses.models import Course, Lesson

# Create your views here.
def detail (request, cid):
    course_item = Course.objects.filter(pk = int(cid))[0]
    lessons = Lesson.objects.filter(course_id = int(cid))
    return render(request,'courses/detail.html',{'course':course_item,'lessons':lessons})