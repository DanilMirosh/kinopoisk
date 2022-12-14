from project.config import config
from project.dao.models import Genre, Director, Movie, FavoriteMovies, User
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "FavoriteMovies": FavoriteMovies,
        "User": User,
    }
