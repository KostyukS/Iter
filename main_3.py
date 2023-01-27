# Задание 3.
class FlatIteratorAllLevel:  # Итератор  обрабатывающий списки с любым уровнем вложенности
    def __init__(self, lst):
        self.lst = lst
        self.flag = True
        self.lst1 = []
        self.count = 0

    def itr(self, lst):

        while self.flag:
            self.flag = False
            for item in self.lst:
                if type(item) == list:
                    self.lst1.extend(item)
                    self.flag = True
                else:
                    self.lst1.append(item)
            self.lst = self.lst1
            self.lst1 = []
        return self.lst

    def __iter__(self):
        return self

    def __next__(self):
        lst2 = self.itr(self.lst)
        while self.count < len(lst2):
            self.count += 1
            return lst2[self.count - 1]
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIteratorAllLevel(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIteratorAllLevel(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None,
                                                           '!']
    print('Функция test_3() отработала без ошибок!')


if __name__ == '__main__':
    test_3()
