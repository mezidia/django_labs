from sqlalchemy import Integer, String, Column, Float, DateTime, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False)
    place_from = Column(String(45), nullable=False)
    place_to = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    time = Column(DateTime, nullable=False)
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
