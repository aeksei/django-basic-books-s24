from datetime import datetime
from random import choice

from django.http import HttpRequest, HttpResponse, JsonResponse

from books.models import BOOKS


def current_time(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    return HttpResponse(now)


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Добро пожаловать в библиотеку!!!</h1>")


def random_book(request: HttpRequest) -> HttpResponse:
    return JsonResponse(
        choice(BOOKS),
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False,
        }
    )


def all_books(request: HttpRequest) -> HttpResponse:
    return JsonResponse(
        BOOKS,
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False,
        }
    )
