from django.db import models


class Flight(models.Model):
    plane = models.CharField(max_length=200, null=False)
    destination_from = models.CharField(max_length=200, default='Лос Сантос')
    destination_to = models.CharField(max_length=200, default='Сан Фіерро')
    flight_created = models.DateTimeField(auto_now_add=True)
    departure_date = models.CharField(max_length=200)
    arrival_date = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return f'{self.destination_from} - {self.destination_to}'
