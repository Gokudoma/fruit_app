from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.Charfield(max_length=100)
    color = models.Charfield(max_length=100)
    brand = models.Charfield(max_length=100)
    origin = models.Charfield(max_length=100)

    def __str__(self):
        return self.name