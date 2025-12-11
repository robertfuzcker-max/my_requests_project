import json
import os
from typing import TextIO


def load_movies(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_movies(path: str, movies: list[dict]) -> None:
    f: TextIO
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)

def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
    new_movies = movies.copy()
    if new_movies:
        new_id = max(movie['id'] for movie in new_movies) + 1
    else:
        new_id = 1
    new_movie = {
        "id": new_id,
        "title": title,
        "year": year,
        "watched": False
    }
    new_movies.append(new_movie)
    return new_movies

def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    new_movies = movies.copy()
    for movie in new_movies:
        if movie['id'] == movie_id:
            movie['watched'] = True
            break
    return new_movies

def delete_movie(movies: list[dict], movie_id: int) -> list[dict]:
    new_movies = [movie for movie in movies if movie['id'] != movie_id]
    return new_movies

def find_by_year(movies: list[dict], year: int) -> list[dict]:
    return [movie for movie in movies if movie['year'] == year]
