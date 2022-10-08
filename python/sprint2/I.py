class MyQueueSized:
    """Очень ограниченного размера."""

    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.current_size = 0
        self.queue = [None] * max_size
        self.tail = 0
        self.head = 0

    def push(self, number: int) -> int:
        """Добавляет число в очередь и возвращает его."""
        if self.current_size != self.max_size:
            self.queue[self.tail] = number
            self.tail = (self.tail + 1) % self.max_size
            self.current_size += 1
            return number
        else:
            raise Exception("error")

    def pop(self) -> int:
        """Удаляет первое число из очереди и возвращает его."""
        if self.is_empty():
            return None
        number = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        return number

    def peek(self) -> int:
        """Возвращает первое число из очереди."""
        return self.queue[self.head]

    def size(self) -> int:
        """Возвращает размер очереди."""
        return self.current_size

    def is_empty(self) -> bool:
        return self.current_size == 0


if __name__ == "__main__":
    number_of_commands = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    while number_of_commands != 0:
        number_of_commands -= 1
        command = input()
        try:
            if command == "peek":
                print(queue.peek())
                continue
            if command == "size":
                print(queue.size())
                continue
            if command == "pop":
                print(queue.pop())
                continue
            command_split = command.split()
            if command_split[0] == "push":
                queue.push(int(command_split[1]))
                continue
            raise Exception("Неизвестная команда.")
        except Exception as e:
            print(e)
