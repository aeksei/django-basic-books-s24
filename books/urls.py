from django.urls import path

from books import views


urlpatterns = [
    path("current-time/", views.current_time),
    path("books/random-book/", views.random_book),
    path("", views.index),
    path("books/", views.all_books),
]
