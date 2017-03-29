from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Course

def index(request):
	courses_list = Course.objects.all()
	return render(request, 'index.html', {'courses_list':courses_list, 'description':'На протяжении курса Вы пройдете через все стадии разработки сайта от проектирования интерфейса и структуры данных до программирования функционала и деплоймента. Вы научитесь языку, и освоите технологии и инструменты, которые необходимые web-разработчику, (git/github, html/css, bootstrap, databases, linux, shell, nginx, deployment), научитесь понимать, что именно Вам нужно и где находятся ответы на возникающие вопросы.'})

def contact(request):
	return render(request, "contact.html")

def student_list(request):
	return render(request, "student_list.html")

def student_detail(request):
	return render(request, "student_detail.html")
