from sqlalchemy import Integer, String, Column, PrimaryKeyConstraint, \
    UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


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


engine = create_engine('sqlite:///app.sqlite')

Base.metadata.create_all(engine)

session = Session(bind=engine)

user_max = User(
    name='James',
    age=25,
    gender='male',
    nationality='USA'
)

session.add(user_max)
session.commit()

searched_user = session.query(User).first()
print(searched_user.name)

searched_user.name = 'Maxim'
session.add(searched_user)
session.commit()

searched_user = session.query(User).filter(User.nationality == 'USA').one()
session.delete(searched_user)
session.commit()
