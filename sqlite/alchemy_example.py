from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User, Base

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
