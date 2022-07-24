from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    date_of_birth = models.DateField()