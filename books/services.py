from django.http import Http404

from books import models


def get_object_or_404(model: list[dict], **kwargs) -> dict:
    for object_ in model:
        for key, value in kwargs.items():
            if object_[key] == value:
                return object_

    raise Http404


if __name__ == '__main__':
    book = get_object_or_404(models.BOOKS, id=1)
    print(book)

    book = get_object_or_404(models.BOOKS, id=2)
    print(book)

    category = get_object_or_404(models.CATEGORIES, slug="javascript")
    print(category)
