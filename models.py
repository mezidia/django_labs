from operator import pos
from peewee import Database, Model, CharField, PrimaryKeyField, IntegerField, ForeignKeyField, FloatField
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase, Proxy
from mysql_api import config as ms_config
from postgresql_api import config as ps_config

database_proxy = Proxy()

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

# It is for an example
class User(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    age = IntegerField()
    gender = CharField()
    nationality = CharField()


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database=database_proxy
        order_by='id'


class Car(BaseModel):
    class Meta:
        db_table='cars'


class Place(BaseModel):
    class Meta:
        db_table='places'


class Route(BaseModel):
    place_from = ForeignKeyField(Place)
    place_to = ForeignKeyField(Place)
    price = FloatField()
    car = ForeignKeyField(Car)

    class Meta:
        db_table='routes'


database_proxy.initialize(mysql_database)
database_proxy.create_tables([Car, Place, Route])

database_proxy.initialize(sqlite_database)
database_proxy.create_tables([Car, Place, Route])

database_proxy.initialize(postgresql_database)
database_proxy.create_tables([Car, Place, Route])
