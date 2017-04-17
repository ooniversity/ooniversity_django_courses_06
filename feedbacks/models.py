from django.db import models

# Create your models here.


class Feedback(models.Model):
	name = models.CharField('Имя отправителя', max_length=50)   
	subject = models.CharField('Тема сообщения', max_length=50)
	message = models.TextField('Cообщение')
	from_email = models.EmailField('e-mail отправителя') 
	create_date = models.DateTimeField('Дата создани', auto_now_add=True)
	
	def __str__(self):
            return self.name
	
	

	

