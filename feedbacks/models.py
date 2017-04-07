from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    message = models.TextField()
    from_email = models.EmailField(max_length=254)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name