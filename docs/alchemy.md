# SQLAlchemy

## Overview

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

## Models

We developed our [models](https://github.com/mezidia/medivac/blob/main/models.py) of tables:

```python
from sqlalchemy import Integer, String, Column, Float, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False)
    place_from = Column(String(45), nullable=False)
    place_to = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    car = Column(String(45), nullable=False)

    __table_args__ = (ForeignKeyConstraint(['car'], ['cars.name']),
                      ForeignKeyConstraint(['place_from'], ['places.name']),
                      ForeignKeyConstraint(['place_to'], ['places.name']),)


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False, unique=True)


class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False, unique=True)
```

## Core

Here we show our use of [SQLAlchemy Core](https://docs.sqlalchemy.org/en/14/core/):

### Insert

```python
connection = engine_mysql.connect()
ins = insert(Route)
_ = connection.execute(ins,
                       name=route_name,
                       place_from=place_from,
                       place_to=place_to,
                       price=price,
                       car=car
                       )
```

### Update

```python
connection = engine_mysql.connect()
s = update(Route).where(
    Route.name == route_name
).values(
    place_from=place_from,
    place_to=place_to,
    price=price,
    car=car
)
_ = connection.execute(s)
```

### Delete

```python
connection = engine_mysql.connect()
s = delete(Route).where(Route.name == route_name)
_ = connection.execute(s)
```

### Get

```python
connection = engine_mysql.connect()
s = select([Route]).where(
    Route.name == route_name
)
route = connection.execute(s).first()
```

## Session

Here we show our use of [SQLAlchemy Session](https://docs.sqlalchemy.org/en/14/orm/session.html):

### Insert

```python
car_object = Car(id=car[0], name=car[1])
to_session.add(car_object)
to_session.commit()
```

### Delete

```python
to_session.query(Route).delete()
to_session.query(Place).delete()
to_session.query(Car).delete()
to_session.commit()
```
