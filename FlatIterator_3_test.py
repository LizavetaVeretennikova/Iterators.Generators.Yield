
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.item_list = []
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.list_of_list):
            if self.item_list:
                self.list_of_list, self.counter = self.item_list.pop()
                return next(self)
            else:
                raise StopIteration
        item = self.list_of_list[self.counter]
        self.counter += 1
        if type(item) is not list:
            return item
        else:
            self.item_list.append((self.list_of_list, self.counter))
            self.list_of_list = item
            self.counter = 0
            return next(self)
        raise StopIteration


test = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []],
]
print(list(FlatIterator(test)))

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
