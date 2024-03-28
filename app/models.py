from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Visit(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Visit at {self.datetime} ({self.latitude}, {self.longitude})"
