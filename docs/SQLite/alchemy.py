from datetime import datetime

from sqlalchemy import Index, Integer, String, Column, DateTime, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(String(200), nullable=False, default=False)
    user_id = Column(Integer(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id']),
        Index('title_content_index' 'title', 'content'),  # composite index on title and content
    )


engine = create_engine('sqlite:///app.sqlite')
Base.metadata.create_all(engine)
session = Session(bind=engine)

user_max = User(
    username='Maxim',
    email='mezgoodle@gmail.com',
    password='123456'
)

session.add(user_max)
session.commit()

user = session.query(User).first()
print(user.username)

user.username = 'VsIG'
session.add(user)
session.commit()

user = session.query(User).filter(User.password == '123456').one()
session.delete(user)
session.commit()


