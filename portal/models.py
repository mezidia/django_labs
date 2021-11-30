from django.db import models


class Flight(models.Model):
    id = models.IntegerField(primary_key=True)
    plane = models.CharField(max_length=200, null=False)
    destination_from = models.CharField(max_length=200, default='Лос Сантос')
    destination_to = models.CharField(max_length=200, default='Сан Фіерро')
    flight_created = models.DateTimeField(auto_now_add=True)
    departure_date = models.CharField(max_length=200)
    arrival_date = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    price = models.FloatField()
