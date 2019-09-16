from django.db import models
from django.urls import reverse
from datetime import date

from django.contrib.auth.models import User

# Create your models here.


CONTAINERS = (
    ('T', 'Tap'),
    ('B', 'Bottle'),
    ('C', 'Can'),
)



class Beer(models.Model):
    name = models.CharField(max_length=100)
    brewer = models.CharField(max_length=100)
    abv = models.FloatField()
    ibu = models.IntegerField()
    style = models.CharField(max_length=100)
    taste_profile = models.TextField(max_length=750)
    container_type = models.CharField(
        max_length = 1,
        choices = CONTAINERS,
        default = CONTAINERS[0][0]
    )


    def __str__(self):
        return self.name

class LikeBeerUser(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.beer} in {self.user}'s Cooler" 

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    beers_on_tap = models.ManyToManyField(Beer)

    def __str__(self):
        return self.name
