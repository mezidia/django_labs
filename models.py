from peewee import Database, Model, CharField, PrimaryKeyField, IntegerField, ForeignKeyField, FloatField
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase
from mysql_api import config as ms_config
from postgresql_api import config as ps_config

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
    port=3307,
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


class Car(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database=mysql_database
        order_by='id'
        db_table='cars'


class Place(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()

    class Meta:
        database=mysql_database
        order_by='id'
        db_table='places'


class Route(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    place_from = ForeignKeyField(Place)
    place_to = ForeignKeyField(Place)
    price = FloatField()
    car = ForeignKeyField(Car)

    class Meta:
        database=mysql_database
        order_by='id'
        db_table='routes'

mysql_database.create_tables([Car, Place, Route]) # типу створити таблиці завчасно