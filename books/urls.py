from django.urls import path

from books import views


urlpatterns = [
    path("current-time/", views.current_time),
    path("books/random-book/", views.random_book),
    path("", views.index),
    path("books/", views.all_books),
    path("books/<int:book_id>/", views.get_detail_book),
    path("books/published_year/<int:book_id>/", views.get_detail_book),
    path("categories/<slug:category_slug>/books/", views.get_books_by_category),
]
