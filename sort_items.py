from operator import itemgetter

# def itemgetter(index: int):
#     # index - локальная для функции itemgetter
#     def _itemgetter(tuple_: tuple):
#         # index - nonlocal для функции _itemgetter
#         # tuple_ - локальная для функции _itemgetter
#         return tuple_[index]
#     return _itemgetter


if __name__ == "__main__":
    list_ = [("a", 3), ("c", 1), ("b", 2)]

    itemgetter_1 = itemgetter(1)

    print(sorted(list_, key=itemgetter_1))
    list_.sort(key=itemgetter(1))
    print(list_)
