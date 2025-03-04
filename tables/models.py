from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Стол {self.number} ({self.seats} мест)"


# Create your models here.
