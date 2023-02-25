from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.PositiveIntegerField(unique=True)
    city = models.CharField(max_length=100)