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

class People_Limbs(models.Model):
    person = models.OneToOneField(
        People,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    arm=models.IntegerField()
    leg=models.IntegerField()
    feet=models.IntegerField()
    hands=models.IntegerField()