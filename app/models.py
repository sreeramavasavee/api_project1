from django.db import models

# Create your models here.
class employee(models.Model):
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    ejob=models.CharField(max_length=100)