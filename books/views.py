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
    query_params = request.GET
    query_published_year = query_params.get("published_year")

    books = BOOKS.copy()
    if query_published_year is not None:
        query_published_year = int(query_published_year)
        books = [
            book
            for book in books
            if book["published_year"] == query_published_year
        ]

    return JsonResponse(
        books,
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
