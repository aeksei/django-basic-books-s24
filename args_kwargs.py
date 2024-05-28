# Пример функции, принимающей и печатающей информацию о персоне
def print_person(first_name, second_name, age):
    print(f"Имя: {first_name}, Фамилия: {second_name}, Возраст: {age}")


def common(*args, **kwargs):
    print(*args)
    print(kwargs)


if __name__ == '__main__':
    # a = 1, 2, 3
    # print(a)
    #
    # b, c, d = a
    # print(a)
    # print(*a)  # print(b, c, d) или print(a[0], c, d)
    #
    # person_info = {
    #     'second_name': 'Иванов',
    #     'first_name': 'Иван',
    #     'age': 25
    # }
    # print_person(**person_info)

    common(arg_1=1, arg_2=2)

    print(1, 2, 3, sep="-")
