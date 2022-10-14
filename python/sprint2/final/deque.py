# ID посылки: 71847312
from typing import Any


class ArraySizeError(Exception):
    """Вызывается, когда массив переполнен или пуст."""

    pass


class Deque:
    """Двухпоточная очередь - дек."""

    def __init__(self, max_size: int) -> None:
        self.__front = 0
        self.__back = 0
        self.__max_size = max_size
        self.__items = [None] * max_size
        self.__current_size = 0

    def push_back(self, value: Any) -> None:
        """Добавить элемент в конец дека."""
        if self._is_full():
            raise ArraySizeError("Дек заполнен.")
        self.__back = (self.__back - 1) % self.__max_size
        if self.__back < 0:
            self.__back = self.__max_size + self.__back
        if self._is_empty():
            self.__front = self.__back
        self._add_item(value, self.__back)

    def push_front(self, value: Any) -> None:
        """Добавить элемент в начало дека."""
        if self._is_full():
            raise ArraySizeError("Дек заполнен.")
        self.__front = (self.__front + 1) % self.__max_size
        if self._is_empty():
            self.__back = self.__front
        self._add_item(value, self.__front)

    def pop_front(self) -> Any:
        """Вывести первый элемент дека и удалить его."""
        value = self._pop_item(self.__front)
        self.__front = (self.__front - 1) % self.__max_size
        if self.__front < 0:
            self.__front = self.__max_size + self.__front
        return value

    def pop_back(self) -> Any:
        """Вывести последний элемент дека и удалить его."""
        value = self._pop_item(self.__back)
        self.__back = (self.__back + 1) % self.__max_size
        return value

    def _pop_item(self, cursor: int) -> Any:
        """Удаление и возвращение элемента по указателю."""
        if self._is_empty():
            raise ArraySizeError("Дек пуст.")
        value = self.__items[cursor]
        self.__items[cursor] = None
        self.__current_size -= 1
        return value

    def _add_item(self, value: Any, cursor: int) -> None:
        """Добавление элемента по указателю."""
        self.__items[cursor] = value
        self.__current_size += 1

    def _is_empty(self) -> bool:
        """Возвращает True, если дек пуст."""
        return self.__current_size == 0

    def _is_full(self) -> bool:
        """Возвращаешь True, если дек заполнен."""
        return self.__current_size == self.__max_size


if __name__ == "__main__":
    number_of_commands = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    while number_of_commands > 0:
        number_of_commands -= 1
        try:
            command = input().split()
            method = getattr(deque, command[0])
            if len(command) == 2:
                method(int(command[1]))
                continue
            print(method())
            continue
        except ArraySizeError:
            print("error")
