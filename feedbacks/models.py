from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=64)
    subject  = models.CharField(max_length=255)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name