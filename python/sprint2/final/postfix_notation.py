# ID посылки: 71847637
import re
from typing import Any, List

ALLOWED_OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: y - x,
    "*": lambda x, y: x * y,
    "/": lambda x, y: y // x,
}


class ArraySizeError(Exception):
    """Вызывается, когда массив переполнен или пуст."""

    pass


class Stack:
    """Стек с добавлением и удаление элементов."""

    def __init__(self) -> None:
        self.__items: list = []

    def push(self, value: Any) -> Any:
        """Добавляет элемент в стек и возвращает его."""
        self.__items.append(value)
        return value

    def pop(self) -> Any:
        """Удаляет элемент с вершины стека и возвращает его."""
        if not self.__items:
            raise ArraySizeError("Стек пуст.")
        return self.__items.pop()


def calculation(expression: List[str]) -> int:
    """Чтение постфиксной нотации и вычисление результата."""
    stack = Stack()
    for elem in expression:
        operand_search = re.search(r"\d+", elem)
        if operand_search:
            stack.push(int(elem))
            continue
        operation = ALLOWED_OPERATIONS.get(elem)
        if operation is None:
            raise KeyError(f"Символ {elem} не соответствует разрешенным.")
        operation_result = operation(stack.pop(), stack.pop())
        stack.push(operation_result)
        continue
    return stack.pop()


def read_input() -> List[str]:
    expression = input().split()
    return expression


if __name__ == "__main__":
    expression = read_input()
    print(calculation(expression))
