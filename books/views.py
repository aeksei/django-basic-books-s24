from datetime import datetime
from random import choice

from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
    Http404,
)

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
        safe=False,  # Списки будут серриализоваться
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False,
        }
    )


def get_detail_book(request, book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return JsonResponse(
                book,
                json_dumps_params={
                    "indent": 4,
                    "ensure_ascii": False,
                }
            )

    raise Http404


def my_custom_page_not_found_view(request: HttpRequest, exception) -> HttpResponse:
    return HttpResponse("Страница не найдена :(", status=404)
