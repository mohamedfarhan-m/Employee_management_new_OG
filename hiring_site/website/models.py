from django.db import models

# Create your models here.
class Stdent(models.Model):
    name=models.CharField(max_length=200)
    college=models.CharField(max_length=200)
    age=models.IntegerField()
    is_Active=models.BooleanField(default=False)

