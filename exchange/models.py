from django.db import models


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    places = models.PositiveIntegerField()
    deadline = models.DateField()
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.university
