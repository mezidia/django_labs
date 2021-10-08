## Overview

In case we are using _peewee_, we have created models which are common for all database.

## Models

Here you can see all models, which we have created:

* ### BaseModel

```python
class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True)

    class Meta:
        database = database_proxy
        order_by = 'id'
```

* ### Car

```python
class Car(BaseModel):
    class Meta:
        db_table = 'cars'
```

* ### Place

```python
class Place(BaseModel):
    class Meta:
        db_table = 'places'
```

* ### Route

```python
class Route(BaseModel):
    place_from = ForeignKeyField(Place, field='name', on_delete='CASCADE')
    place_to = ForeignKeyField(Place, field='name', on_delete='CASCADE')
    price = FloatField()
    car = ForeignKeyField(Car, field='id', on_delete='CASCADE')

    class Meta:
        db_table = 'routes'
```

## Code logic

**BaseModel** has common fields and class _Meta_ and other models inheritance from it.

Then in the [app.py](https://github.com/mezidia/medivac/blob/main/app.py) we connect to all databases:

```python
from mysql_api import config as ms_config
from postgresql_api import config as ps_config

from models import Route, Car, Place, database_proxy
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase, DatabaseError

mysql_database = MySQLDatabase(
    ms_config.db_name,
    host=ms_config.host,
    port=3306,
    user=ms_config.user,
    password=ms_config.password
)

path_to_database = './sqlite3.db'
sqlite_database = SqliteDatabase(path_to_database)

postgresql_database = PostgresqlDatabase(
    ps_config.db_name,
    host=ps_config.host,
    port=5432,
    user=ps_config.user,
    password=ps_config.password
)
```

Next step is creating the tables:

```python
def create_tables():
    """
    Function for creating tables in all three databases
    :return: nothing to return
    """
    database_proxy.initialize(mysql_database)
    database_proxy.create_tables([Car, Place, Route])

    database_proxy.initialize(sqlite_database)
    database_proxy.create_tables([Car, Place, Route])

    database_proxy.initialize(postgresql_database)
    database_proxy.create_tables([Car, Place, Route])
```

And that's all. When we need, we just call `database_proxy.initialize(needed_database)`.
