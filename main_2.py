# Задание 2.
import types


def flat_generator(list_of_lists):  # Генератор  обрабатывающий списки с любым уровнем вложенности
    lst = list_of_lists
    flag = True
    lst1 = []
    count = 0
    while flag:
        flag = False
        for item in lst:
            if type(item) == list:
                lst1.extend(item)
                flag = True
            else:
                lst1.append(item)
        lst = lst1
        lst1 = []
    lst2 = lst
    while count < len(lst2):
        count += 1
        yield lst2[count - 1]


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print('Функция test_2() отработала без ошибок!')


if __name__ == '__main__':
    test_2()
