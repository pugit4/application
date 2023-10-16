from django.db import models

# Create your models here.
class creators(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)