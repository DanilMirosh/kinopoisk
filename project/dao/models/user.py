from sqlalchemy import Column, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from project.setup.db.models import BaseWithID, KeyType


class User(BaseWithID):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String(40))
    surname = Column(String(40))
    favourite_genre = Column(KeyType, ForeignKey("genres.id"))
    favourite_genre_object = relationship("Genre")
    favourite_movies = relationship("Movie", secondary="favorite_movies")
