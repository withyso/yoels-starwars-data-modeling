import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base): 
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), unique=True)
    password = Column(Integer)
    email = Column(String(30), unique=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String(10))

class CharactersFavs(Base):
    __tablename__ = 'charactersfavs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters_relationship = relationship(Characters)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    population = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(20))

class PlanetsFavs(Base):
    __tablename__ = 'planetsfavs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets_relationship = relationship(Planets)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
