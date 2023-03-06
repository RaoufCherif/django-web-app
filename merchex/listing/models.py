from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):


    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

 
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2023)] 
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    types = models.fields.CharField(max_length=50)
    clothings = models.fields.CharField(max_length=500)
   



    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
        title = models.fields.CharField(max_length=100)
        description = models.fields.CharField(max_length=1000)
        version = models.fields.CharField(max_length=10)
   

       #band = models.ForeignKey(Band, on_delete=models.SET_NULL)