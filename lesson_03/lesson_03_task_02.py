from abc import abstractmethod


class NewType:

    def __init__(self, value):
        self._list_data = [value]
        self._access_value = self._list_data[0]

    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def read(self):
        pass


class Queue(NewType):

    def push(self, value):
        self._list_data.append(value)

    def pop(self):
        _len_value = len(self._list_data)
        try:
            if _len_value == 1:
                self._list_data.pop(0)
                self._access_value = None
            else:
                self._list_data.pop(0)
                self._access_value = self._list_data[0]
        except IndexError:
            print("Queue is empty")

    def read(self):
        if len(self._list_data) > 0:
            return self._access_value
        else:
            return "Queue is empty"


class Stack(NewType):

    def push(self, value):
        self._list_data.append(value)
        _len_value = len(self._list_data)
        self._access_value = self._list_data[_len_value - 1]

    def pop(self):
        _len_value = len(self._list_data)
        try:
            if _len_value > 1:
                self._list_data.pop()
                _len_value = len(self._list_data)
                self._access_value = self._list_data[_len_value - 1]
            elif _len_value == 1:
                self._list_data.pop()
                self._access_value = None
        except IndexError:
            print("Stack is empty")

    def read(self):
        if len(self._list_data) > 0:
            return self._access_value
        else:
            return "Stack is empty"


new_stack = Stack(1)
print(new_stack.read())

new_stack.push(2)
print(new_stack.read())

new_stack.pop()
print(new_stack.read())

temp_tuple = (1, 3)
new_stack.push(temp_tuple)
print(new_stack.read())

new_stack.pop()
print(new_stack.read())

new_stack.pop()
print(f'{new_stack.read()}\n\n\n')


new_queue = Queue(3)
print(new_queue.read())

new_queue.push(2)
print(new_queue.read())

new_queue.pop()
print(new_queue.read())

temp_list = [1, 5, 9]
new_queue.push(temp_list)
print(new_queue.read())

new_queue.pop()
print(new_queue.read())

new_queue.pop()
print(new_queue.read())

