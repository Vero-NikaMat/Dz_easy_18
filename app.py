# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение


from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from models import Movie, Director, Genre


def create_app(config_object):
    """функция создания основного объекта app"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        film = Movie(id=21, title="Новый фильм", description="Такого фильма нет, значит и описания нет", trailer = "ссылка", year=2022, rating=0, genre_id=9, director_id=21)
        director_new = Director(id=21, name="Никто")

        # создать несколько сущностей чтобы добавить их в БД

        with db.session.begin():
            db.session.add_all([film, director_new])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)





