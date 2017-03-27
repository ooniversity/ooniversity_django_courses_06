from django.shortcuts import render
from courses.models import Course, Lesson
from coaches.models import Coach


# Create your views here.
def detail (request, cid):
    course_item = Course.objects.filter(pk = int(cid))[0]
    lessons = Lesson.objects.filter(course_id = int(cid))
    trainer=assist=''    
    if course_item.coach_id:
        trainer = Coach.objects.filter(id=course_item.coach.id).first()
    if course_item.assistant_id:
        assist = Coach.objects.filter(id=course_item.assistant.id).first()
    print('====>>{}\n---->>{}'.format(trainer,assist))
    return render(request,'courses/detail.html',
                  {'course':course_item,
                   'lessons':lessons,
                   'coach':trainer,
                   'assistant':assist,})