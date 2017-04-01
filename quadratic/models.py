from django.db import models

class Brand(models.Model):
    brand = models.CharField(max_length=255)

class Car(models.Model):
    name = models.CharField(max_length=255)
    brandx = models.ForeignKey(Brand)

