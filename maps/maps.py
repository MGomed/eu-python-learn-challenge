from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rating(movie: dict) -> float:
            rating = movie["rating_kinopoisk"]
            countries = movie["country"]
            if countries.count(",") >= 1 and rating != "":
                return float(rating)

        filtered_rating = map(get_rating, list_of_movies)
        filtered_rating_list = [
            rating for rating in filtered_rating if rating is not None and rating != 0
        ]

        return sum(filtered_rating_list) / len(filtered_rating_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def filter_name(movie: dict) -> int:
            movie_rating = movie["rating_kinopoisk"]
            if movie_rating != "" and float(movie_rating) >= rating:
                return movie["name"].count("и")

            return 0

        letters_count = map(filter_name, list_of_movies)

        return sum(letters_count)
