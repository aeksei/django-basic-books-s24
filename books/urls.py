from django.urls import path

from books import views


app_name = "books"

urlpatterns = [
    path("current-time/", views.current_time),
    path("books/random-book/", views.random_book),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("books/", views.all_books, name="book-list"),
    path("books/<int:book_id>/", views.get_detail_book, name="book-detail"),
    path("books/published_year/<int:book_id>/", views.get_detail_book),
    path("categories/<slug:category_slug>/books/", views.get_books_by_category),
]
