from time import time
from functools import wraps


def fabric_decorator(*args_for_decorator, **kargs_for_decorator):
    def decorator(fn):  # Сам декоратор принимает только исходную функцию
        # Что-то на момент декорирования
        ...
        def wrapper(*args, **kwargs):  # Все аргументы предназначенные для fn
            # Выполнить что-то до вызова исходной функции
            ...

            result = fn(*args, **kwargs)

            # Выполнить что-то после вызова исходной функции
            ...

            return result  # Вернуть результат исходной функции

        # Что-то после декорирования
        ...
        return wrapper  # Вернуть задекорированную исходную функцию
    return decorator


def decorator(fn):  # Сам декоратор принимает только исходную функцию
    # Что-то на момент декорирования
    ...

    def wrapper(*args, **kwargs):  # Все аргументы предназначенные для fn
        # Выполнить что-то до вызова исходной функции
        ...

        result = fn(*args, **kwargs)

        # Выполнить что-то после вызова исходной функции
        ...

        return result  # Вернуть результат исходной функции

    # Что-то после декорирования
    ...
    return wrapper  # Вернуть задекорированную исходную функцию


def my_time(fn):
    print(f"Я вызываюсь на момент декорирования функции `{fn.__name__}` :)")

    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Выполнить что-то до вызова исходной функции
        t0 = time()

        # Вызов исходной функции, которая сидит в аргументе fn
        result = fn(*args, **kwargs)

        # Выполнить что-то после вызова исходной функции
        dt = time() - t0
        print(f"Время выполнения {dt}")

        return result

    return wrapper


@my_time  # sort_with_sorted = my_time(sort_with_sorted)  # Декорирование
def sort_with_sorted(list_: list) -> list:
    result = sorted(list_)
    return result


@my_time
def sort_with_method(list_: list) -> list:
    """Сортировка встроенным методом."""
    list_.sort()
    return list_


if __name__ == '__main__':
    values = list(range(10 ** 6, 0, -1))

    sort_with_method(values)  # Вызывается wrapper
    print(sort_with_method.__name__)
    print(sort_with_method.__doc__)

    sort_with_method(values)  # Вызывается wrapper

    # sort_with_method(values)
