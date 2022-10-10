from typing import Optional


class Node:
    """Узел двусвязного списка."""

    def __init__(
        self,
        value: int,
        next_item: Optional["Node"] = None,
        prev_item: Optional["Node"] = None,
    ):
        self.value = value
        self.next_item = next_item
        self.prev_item = prev_item


class MyListQueue:
    """Очередь на связанном списке."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.current_size: int = 0

    def get(self) -> int:
        """Вывести элемент, находящийся в голове очереди, и удалить его."""
        if self.current_size == 0:
            raise Exception("error")
        current_head = self.head
        self.head = current_head.prev_item
        if self.head is None:
            self.tail = None
        else:
            self.head.next_item = None
        self.current_size -= 1
        return current_head.value

    def put(self, number: int):
        """Добавить число в очередь."""
        current_tail = self.tail
        self.tail = Node(number, next_item=current_tail)
        if current_tail is None:
            self.head = self.tail
        else:
            current_tail.prev_item = self.tail
        self.current_size += 1

    def size(self) -> int:
        """Вывести текущий размер очереди."""
        return self.current_size


if __name__ == "__main__":
    number_of_commands = int(input())
    queue = MyListQueue()
    while number_of_commands > 0:
        number_of_commands -= 1
        try:
            command = input()
            if command == "get":
                print(queue.get())
                continue
            if command == "size":
                print(queue.size())
                continue
            command_split = command.split()
            if command_split[0] == "put":
                queue.put(int(command_split[1]))
                continue
            raise Exception("Неизвестная команда.")
        except Exception as e:
            print(e)
