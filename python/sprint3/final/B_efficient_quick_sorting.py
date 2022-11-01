# ID посылки: 73507941
import random
from typing import List
from collections import namedtuple


def in_place_quick_sort(participants: List) -> None:
    """Быстрая сортировка с потреблением доп. памяти O(1)."""
    left = 0
    right = len(participants) - 1
    partition(participants, left, right)


def partition(participants: List, left: int, right: int) -> None:
    """Переупорядочивание участка массива относительно опорного элемента."""
    pivot = participants[random.randint(left, right)]
    l_index = left
    r_index = right
    while l_index <= r_index:
        if participants[r_index] <= pivot < participants[l_index]:
            participants[l_index], participants[r_index] = (
                participants[r_index],
                participants[l_index],
            )
            l_index += 1
            r_index -= 1
        if participants[l_index] <= pivot:
            l_index += 1
        if pivot < participants[r_index]:
            r_index -= 1
    if r_index > left:
        partition(participants, left, r_index)
    if l_index < right:
        partition(participants, l_index, right)


def read_input() -> List:
    number_of_participants = int(input())
    Participant = namedtuple(
        "Participant", ["solved_tasks", "fine", "username"]
    )
    participants = []
    for _ in range(number_of_participants):
        row = input().split()
        participants.append(Participant(-int(row[1]), int(row[2]), row[0]))
    return participants


if __name__ == "__main__":
    participants = read_input()
    in_place_quick_sort(participants)
    print("\n".join(list(map(lambda x: x.username, participants))))
