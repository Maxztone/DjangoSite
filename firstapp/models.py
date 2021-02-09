from django.db import models


class Dishes(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.id}: {self.name}'
