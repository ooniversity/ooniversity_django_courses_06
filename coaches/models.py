from django.db import models
from django.conf import settings

class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.user.username

    def get_name(self):
        return '%s' % (self.user.first_name)
    get_name.short_description = 'name'
    # name = property(_get_user_first_name)

    def get_surname(self):
        return '%s' % (self.user.last_name)
    get_surname.short_description = 'surname'
    # surname = property(_get_user_last_name)

    def get_email(self):
        return '%s' % (self.user.email)
    get_email.short_description = 'email'
