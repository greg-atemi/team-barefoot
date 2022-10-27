from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    # pk
    brand = models.CharField(max_length=40)
    year = models.IntegerField()

    def __str__(self):
        return f"Car is {self.brand} {self.year}"


class Review(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.first_name} {self.surname} rates it at {self.rating} out of 10"

