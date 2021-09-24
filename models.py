from sqlalchemy import Integer, String, Column, PrimaryKeyConstraint, UniqueConstraint, Float, DateTime, \
    ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# It is for an example
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(100), nullable=False)
    nationality = Column(String(200), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('name'),
    )


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    place_from = Column(String(45), nullable=False)
    place_to = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    time = Column(DateTime, nullable=False)
    car = Column(Integer, nullable=False)

    __table_args__ = (ForeignKeyConstraint(['car'], ['cars.id']),)


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(45), nullable=False)
