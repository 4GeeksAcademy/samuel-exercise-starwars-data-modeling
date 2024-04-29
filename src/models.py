import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):

    __tablename__ ='users'
    id = Column(Integer, primary_key= True)
    username = Column(String(250))
    email = Column(String(200))
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship("Favorite")

class Favorite(Base):
    __tablename__='favorites'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Planet(Base):

    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    terrain = Column(String(100))
    population = Column(Integer)
    climate = Column(String(100))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    gender = Column(String(50))
    species = Column(String(100))
    birth_year = Column(String(20))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
