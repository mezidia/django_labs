from sqlalchemy import Integer, String, Column, DateTime, \
 ForeignKeyConstraint, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    place_from = Column(String(45), nullable=False)
    place_to = Column(String(45), nullable=False)
    price = Column(Float, nullable=False)
    time = Column(DateTime(), nullable=False)
    car = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint(['car'], ['car.id']),
    )


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)


engine = create_engine('')
Base.metadata.create_all(engine)
session = Session(bind=engine)

car_Medivac = Car(
    id = 3,
    name = 'medivac'
)

route_Dragon_Shrine = Route(
    id = 4,
    name = 'FIRST SILVER EXPRESS',
    place_from = 'ALTERAC PASS',
    place_to = 'DRAGON SHRINE',
    price = 200,
    time = '2021-09-22 22:15:00',
    car = car_Medivac.id
)

session.add(car_Medivac)
session.commit()

session.add(route_Dragon_Shrine)
session.commit()