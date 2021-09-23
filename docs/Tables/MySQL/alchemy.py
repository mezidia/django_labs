from sqlalchemy import Integer, String, Column, DateTime, Float,\
PrimaryKeyConstraint, ForeignKeyConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from config import *

Base = declarative_base()


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer)
    name = Column(String(45), nullable=False)
    place_from = Column(String(45), nullable=False)
    place_to = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    time = Column(DateTime(), nullable=False)
    car = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='id_pk'),
        ForeignKeyConstraint(['car'], ['car.id']),
    )


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer)
    name = Column(String(45), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='id_pk'),
    )


engine = create_engine(f'mysql://{user}:{password}@{localhost}/{db_name}')
Base.metadata.create_all(engine)
session = Session(bind=engine)

car_Medivac = Car(
    name = 'medivac'
)

session.add(car_Medivac)

session.commit()

route_Dragon_Shrine = Route(
    name = 'FIRST SILVER EXPRESS',
    place_from = 'ALTERAC PASS',
    place_to = 'DRAGON SHRINE',
    price = 200,
    time = '2021-09-22 22:15:00',
    car = car_Medivac.id
)

session.add(route_Dragon_Shrine)

session.commit()
