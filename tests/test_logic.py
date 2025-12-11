import os

import pytest

from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year, delete_movie


@pytest.fixture
def test_file():
    path = "test_movies.json"
    yield path
    if os.path.exists(path):
        os.remove(path)


def test_load_movies_no_file():
    movies = load_movies("nonexistent.json")
    assert movies == []


def test_add_movie(test_file):
    movies = []
    new_movies = add_movie(movies, "Test Movie", 2020)
    assert len(new_movies) == 1
    assert new_movies[0]["title"] == "Test Movie"
    assert new_movies[0]["year"] == 2020
    assert new_movies[0]["watched"] == False
    assert new_movies[0]["id"] == 1


def test_mark_watched():
    movies = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    updated = mark_watched(movies, 1)
    assert updated[0]["watched"] == True

    movies2 = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    not_found = mark_watched(movies2, 999)
    assert len(not_found) == 1
    assert not_found[0]["watched"] == False


def test_delete_movie():
    movies = [
        {"id": 1, "title": "Movie1", "year": 2020, "watched": False},
        {"id": 2, "title": "Movie2", "year": 2021, "watched": True}
    ]
    updated = delete_movie(movies, 1)
    assert len(updated) == 1
    assert updated[0]["id"] == 2

    not_found = delete_movie(movies, 999)
    assert len(not_found) == 2  # список не изменился


def test_find_by_year():
    movies = [
        {"id": 1, "title": "Movie1", "year": 2020, "watched": False},
        {"id": 2, "title": "Movie2", "year": 2021, "watched": True}
    ]
    found = find_by_year(movies, 2020)
    assert len(found) == 1
    assert found[0]["title"] == "Movie1"

    empty = find_by_year(movies, 2022)
    assert empty == []


def test_save_load(test_file):
    movies = [{"id": 1, "title": "Test", "year": 2020, "watched": False}]
    save_movies(test_file, movies)

    loaded = load_movies(test_file)
    assert loaded == movies
