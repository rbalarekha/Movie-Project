from . import movies
import os
from flask import Flask


def test_movies_endpoint_returns_200():
    app = Flask(__name__)
    app.register_blueprint(movies.movies_api, url_prefix="/")
    with app.test_client() as client:
        status_code = os.getenv("FAIL_TEST", 200)
        response = client.get("/movies/")
        assert response.status_code == status_code


def test_movies_endpoint_returns_json():
    app = Flask(__name__)
    app.register_blueprint(movies.movies_api, url_prefix="/")
    with app.test_client() as client:
        response = client.get("/movies/")
        assert response.content_type == "application/json"


def test_movies_endpoint_returns_valid_data():
    app = Flask(__name__)
    app.register_blueprint(movies.movies_api, url_prefix="/")
    with app.test_client() as client:
        response = client.get("/movies/")
        data = response.get_json()
        assert isinstance(data, dict)
        assert "movies" in data
        assert isinstance(data.get("movies"), list)
        assert len(data["movies"]) > 0
        assert "title" in data["movies"][0]
