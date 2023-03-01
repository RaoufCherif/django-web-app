from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_lenght=100)
