from typing import Union, Any
from flask import Flask, request, jsonify
from http import HTTPStatus


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users: dict[str, dict] = {}

        @app.route("/user", methods=["POST"])
        def create_user() -> Union[Any, HTTPStatus]:
            req = request.get_json()
            if "name" not in req:
                return (
                    jsonify({"errors": {"name": "This field is required"}}),
                    HTTPStatus.UNPROCESSABLE_ENTITY,
                )

            name = req["name"]
            users[name] = {}
            return (
                jsonify({"data": f"User {name} is created!"}),
                HTTPStatus.CREATED,
            )

        @app.route("/user/<name>", methods=["GET"])
        def get_user(name: str) -> Union[Any, HTTPStatus]:
            if name not in users:
                return "", HTTPStatus.NOT_FOUND

            return (
                jsonify({"data": f"My name is {name}"}),
                HTTPStatus.OK,
            )

        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name: str) -> Union[Any, HTTPStatus]:
            req = request.get_json()
            if "name" not in req:
                return "", HTTPStatus.NOT_FOUND

            new_name = req["name"]
            users[new_name] = users.pop(name)
            return (
                jsonify({"data": f"My name is {new_name}"}),
                HTTPStatus.OK,
            )

        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name: str) -> Union[Any, HTTPStatus]:
            if name not in users:
                return "", HTTPStatus.NOT_FOUND

            users.pop(name)
            return "", HTTPStatus.NO_CONTENT
