

class MyList(list):
    def __init__(self):
        super(MyList, self).__init__()
        self._data = []

    def __getitem__(self, item):
        if self._key_is_valid(item):
            return self._data[item]

    def __setitem__(self, key, value):
        if self._key_is_valid(key):
            self._data[key] = value

    def __delitem__(self, key):
        if self._key_is_valid(key):
            del self._data[key]

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor+1 <= len(self._data):
            temp_value = self._data[self.cursor]
            self.cursor += 1
            return temp_value
        else:
            raise StopIteration

    def _key_is_valid(self, index):
        if 0 < index < len(self._data):
            return True
        else:
            raise IndexError

    def pop(self, key=-1):
        if self._key_is_valid(key):
            del self._data[key-1]

    def append(self, value):
        self._data.extend(self.get_list_for_append(value))

    def insert(self, key, value):
        if self._key_is_valid(key):
            self._data.extend(self.get_list_for_append(0))
            for index in range(len(self._data)):
                self._data[len(self._data) - 1 - index] = self._data[len(self._data) - 1 - index - 1]
                if len(self._data) - 1 - index == key:
                    self._data[key - 1] = value
                    break
            return self._data[key]

    def remove(self, value):
        is_removed = False
        for index in range(len(self._data)):
            if self._data[index] == value:
                self._data.pop(index)
                is_removed = True
                break
        if not is_removed:
            raise ValueError

    def clear(self):
        size = len(self._data)
        if size > 0:
            for index in range(size):
                del self._data[size - 1 - index]

    def __add__(self, other):
        temp_list = [0]
        temp_list.extend(self._data)
        temp_list.extend(other.get_list())
        return MyList(temp_list)

    def print_(self):
        print(self._data)

    def get_list(self):
        return self._data

    @staticmethod
    def get_list_for_append(value):
        return [value]
