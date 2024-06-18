import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    second_name = Column(String(250))

    followeds = relationship('followed', back_populates='post')

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table post.
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_date = Column(String(250))
    
    user = relationship(User)
    comments = relationship('Comment', back_populates='post')

    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table comment
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_author = Column(String(250), nullable=False)
    comment_text = Column(String(250), nullable=False)
    comment_date = Column(String(250), nullable=False)
    
    comment = relationship(Post)

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table follower
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    second_name = Column(String(250))

    follower = relationship(User)

    def to_dict(self):
        return {}
    
class Followed(Base):

    __tablename__ = 'followed'
    # Here we define columns for the table followed
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    second_name = Column(String(250))

    

    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
