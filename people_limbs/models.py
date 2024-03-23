from django.db import models
from people_collection.models import People

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