from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach


# Create your views here.
def detail (request, cid):
    course_item = Course.objects.filter(pk = int(cid))[0]
    lessons = Lesson.objects.filter(course_id = int(cid))
    trainer = Coach.objects.filter(id=course_item.coach.id).first() or ''
    assist = Coach.objects.filter(id=course_item.assistant.id).first() or ''
    return render(request,'courses/detail.html',
                  {'course':course_item,
                   'lessons':lessons,
                   'coach':trainer,
                   'assistant':assist,})