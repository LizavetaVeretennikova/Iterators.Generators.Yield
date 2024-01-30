class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = 0
        self.current_item = 0
        self.stopped = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stopped:
            while self.current_list < len(self.list_of_list):
                if self.current_item < len(self.list_of_list[self.current_list]):
                    item = self.list_of_list[self.current_list][self.current_item]
                    self.current_item += 1
                    return item
                self.current_list += 1
                self.current_item = 0
            self.stopped = True
        raise StopIteration

test = FlatIterator([
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ])
for item in test:
    print(item)

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
