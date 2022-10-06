from typing import Optional


class StackMax:
    """Стэк с возможностью определения максимума среди всех элементов."""

    def __init__(self) -> None:
        self.items: list = []
        self.max: list = []

    def push(self, number: int) -> int:
        """Добавляет число в стек и возвращает его."""
        self.items.append(number)
        if not self.max or self.max[-1] <= number:
            self.max.append(number)
        return number

    def pop(self) -> int:
        """Удаляет число с вершины стека и возвращает его."""
        if not self.items:
            raise Exception("error")
        top = self.items.pop()
        if top == self.max[-1]:
            self.max.pop()
        return top

    def get_max(self) -> Optional[int]:
        """Возвращает максимальное число среди всех элементов."""
        if self.max:
            return self.max[-1]
        return None


if __name__ == "__main__":
    number_of_commands = int(input())
    stack = StackMax()
    while number_of_commands > 0:
        number_of_commands -= 1
        command = input()
        try:
            if command == "get_max":
                print(stack.get_max())
                continue
            if command == "pop":
                stack.pop()
                continue
            command = command.split()
            if command[0] == "push":
                stack.push(int(command[1]))
                continue
            else:
                raise Exception(f"Неизвестная команда {command}")
        except Exception as error:
            print(error)
