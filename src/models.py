import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True)
    diameter = Column(Float, nullable=True)
    rotation_period = Column(Float, nullable=True)
    gravity = Column(Float, nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    surface_water = Column(String(250), nullable=True)
    

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(16), nullable=True)
    eye_color = Column(String(16), nullable=True)
    sex = Column(String(16), nullable=True)
    homeworld = Column(String(250), ForeignKey('planet.name'))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), primary_key=True)
    model = Column(String(250), nullable=True)
    vehicle_class = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Float, nullable=True)
    crew = Column(Integer, nullable=True)
    passengers = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Float, nullable=True)
    cargo_capacity = Column(Float, nullable=True)
    consumables = Column(String(250), nullable=True)
    films = Column(String(250), nullable=True)
    pilots = Column(String(250), nullable=True)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), primary_key=True)
    email = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    planet = relationship(Planet)
    character = relationship(Character)
    vehicle = relationship(Vehicle)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    title = Column(String(250), nullable=False)
    body = Column(String(3200), nullable=False)


class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment = Column(String(1600), nullable=False )
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, nullable=False)
    post = relationship(Post)
    user = relationship(User)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
