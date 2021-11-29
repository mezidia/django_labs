# SQLAlchemy

## Overview

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and
flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing
database access, adapted into a simple and Pythonic domain language.

## Models

We developed our [models](https://github.com/mezidia/medivac/blob/main/app.py#L10-L22) of tables:

```python
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plane = db.Column(db.String(200), nullable=False)
    destination_from = db.Column(db.String(200), default='Лос Сантос')
    destination_to = db.Column(db.String(200), default='Сан Фіерро')
    flight_created = db.Column(db.DateTime, default=datetime.utcnow())
    departure_date = db.Column(db.String(200))
    arrival_date = db.Column(db.String(200))
    duration = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Flight {self.id}>'
```

## Query

Since our task was not to use _ORM_, not many methods have been written, but there is one:

### Get all flights

```python
available_flights = Flight.query.order_by(Flight.flight_created).all()
```

### Get a single flight

```python
founded_flight = Flight.query.get_or_404(id)
```
