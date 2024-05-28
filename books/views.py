from datetime import datetime
from random import choice

from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
    Http404,
)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.models import BOOKS, CATEGORIES
from books.services import get_object_or_404


def current_time(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    return HttpResponse(now)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    template_name = "index.html"
    context = {
        "books_list": BOOKS,
    }
    return render(request, template_name, context)


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
    template_name = "books/book_list.html"
    context = {
        "books_list": books,
    }
    return render(request, template_name, context)


def get_detail_book(request, book_id: int):
    template_name = "books/book_detail.html"
    book = get_object_or_404(BOOKS, id=book_id)
    context = {
        "book_dict": book
    }
    return render(request, template_name, context)


def my_custom_page_not_found_view(request: HttpRequest, exception) -> HttpResponse:
    return HttpResponse("Страница не найдена :(", status=404)


def get_books_by_category(request, category_slug: str):
    category = get_object_or_404(CATEGORIES, slug=category_slug)

    return JsonResponse(
        [
            book
            for book in BOOKS
            if book["category"] == category["slug"]
        ],
        safe=False,  # Списки будут серриализоваться
        json_dumps_params={
            "indent": 4,
            "ensure_ascii": False,
        }
    )


def about(request):
    template_name = "about.html"
    return render(request, template_name)
