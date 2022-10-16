from typing import List, Tuple


def bubble_sort(
    number_of_elements: int, unsorted_list: List[int]
) -> List[int]:
    """Пузырьковая сортировка."""
    for i in range(number_of_elements - 1):
        swaps = 0
        for j in range(number_of_elements - 1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = (
                    unsorted_list[j + 1],
                    unsorted_list[j],
                )
                swaps += 1
        if swaps == 0:
            if i == 0:
                print(" ".join(list(map(str, unsorted_list))))
            break
        print(" ".join(list(map(str, unsorted_list))))
    return unsorted_list


def read_input() -> Tuple[int, List[int]]:
    number_of_elements = int(input())
    unsorted_list = list(map(int, input().split()))
    return number_of_elements, unsorted_list


if __name__ == "__main__":
    number_of_elements, unsorted_list = read_input()
    bubble_sort(number_of_elements, unsorted_list)
