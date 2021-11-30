# SQLAlchemy

## Overview

Once you’ve created your data models, Django automatically gives you a database-abstraction API that lets you create,
retrieve, update and delete objects. This document explains how to use this API. Refer to the data model reference for
full details of all the various model lookup options.

## Models

We developed our [models](https://github.com/mezidia/medivac/blob/main/portal/models.py) of tables:

```python
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
```

## Query

Since our task was not to use _ORM_, not many methods have been written, but there is one:

### Get all flights

```python
flights_data = Flight.objects.all().order_by('-flight_created')
```

### Get a single flight

```python
flight_object = Flight.objects.get(pk=id)
```
