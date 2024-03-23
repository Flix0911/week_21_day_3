from django.db import models

# Create your models here.

class People(models.Model):
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    country_of_origin=models.CharField(max_length=100)
    ssn=models.IntegerField()
    age=models.IntegerField()
    

# Create your models here.
