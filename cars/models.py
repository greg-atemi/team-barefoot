from django.db import models


class Car(models.Model):
    # pk
    brand = models.CharField(max_length=40)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand} {self.year}"