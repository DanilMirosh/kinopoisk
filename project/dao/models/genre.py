from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from project.setup.db.models import BaseWithID


class Genre(BaseWithID):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)
    movies = relationship("Movie", back_populates="genre")
