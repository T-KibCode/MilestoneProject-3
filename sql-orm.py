import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

db = create_engine('postgresql://' + url.username + ':' + url.password + '@' + url.hostname + ':' + str(url.port) + '/' + url.path[1:]) # type: ignore
base = declarative_base()

class Movie(base):
    __tablename__ = 'movie'
    MovieId = Column(Integer, primary_key=True)
    Title = Column(String)
    RelaseYear = Column(Integer)
    Rating = Column(Float)
    ActorId = Column(Integer, ForeignKey('actor.ActorId'))

class Actor(base):
    __tablename__ = 'actor'
    ActorId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    MovieId = Column(Integer, ForeignKey('movie.MovieId'))

class MovieActor(base):
    __tablename__ = 'movie_actor'
    MovieId = Column(Integer, ForeignKey('movie.MovieId'), primary_key=True)
    ActorId = Column(Integer, ForeignKey('actor.ActorId'), primary_key=True)
    movie = relationship('Movie', backref='movie_actor')
    actor = relationship('Actor', backref='movie_actor')

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

actor = session.query(Actor)
for Actor in actor:
    print(Actor.FirstName, Actor.LastName, Actor.MovieId)

movie = session.query(Movie)
for Movie in movie:
    print(Movie.MovieId , Movie.RelaseYear, Movie.Rating, Movie.ActorId)

session.commit()
session.close()
