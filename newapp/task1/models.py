from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(decimal_places=2, max_digits=10)  # Позволяет до 99999999.99
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=10)  # Позволяет до 99999999.99
    size = models.DecimalField(decimal_places=3, max_digits=10)  # Позволяет до 9999.999
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title
