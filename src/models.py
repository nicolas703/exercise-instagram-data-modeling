# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from eralchemy import render_er

# Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String(250))
    post_id = Column(Integer)
    #Post = relationship(Post)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('media.post_id') , primary_key=True)
    user_id = Column(Integer)
    Media = relationship(Media)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('post.user_id') , primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250), nullable=False)
    email = Column(Integer)
    Post = relationship(Post)


    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)


class Comment(Base):
    __tablename__ = 'commeent'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(String(250), ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    Follower = relationship(Follower)
    User = relationship(User)


    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')