from logic import load_movies, save_movies, add_movie, mark_watched, delete_movie, find_by_year

DATA_FILE = "movies.json"


def print_movies(movies: list[dict]):
    if not movies:
        print("Фильмы не найдены.")
        return
    for movie in movies:
        status = "✓" if movie['watched'] else "✗"
        print(f"{movie['id']}. {movie['title']} ({movie['year']}) {status}")


def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\n=== Каталог фильмов ===")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Отметить фильм как просмотренный")
        print("4. Удалить фильм")
        print("5. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print_movies(movies)
        elif choice == "2":
            title = input("Название фильм: ").strip()
            year = int(input("Год выпуска: "))
            movies = add_movie(movies, title, year)
            save_movies(DATA_FILE, movies)
            print("Фильм добавлен!")
        elif choice == "3":
            print_movies(movies)
            movie_id = int(input("ID фильа: "))
            movies = mark_watched(movies, movie_id)
            save_movies(DATA_FILE, movies)
            print("Статус обновлён!")
        elif choice == "4":
            print_movies(movies)
            movie_id = int(input("ID фильма для удаления: "))
            movies = delete_movie(movies, movie_id)
            save_movies(DATA_FILE, movies)
            print("Фильм удалён!")
        elif choice == "5":
            year = int(input("Год выпуска: "))
            found = find_by_year(movies, year)
            print(f"\nФильмы {year} года:")
            print_movies(found)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()
