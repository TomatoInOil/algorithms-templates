from typing import List

MAXIMUM_OF_DIGITS = 4


def number_weight(x):
    while len(x) < MAXIMUM_OF_DIGITS:
        x += x
    return x


def make_larger_number(list_of_numbers: List[str]) -> str:
    """Составляет наибольшее число из переданных чисел."""
    list_of_numbers.sort(key=number_weight, reverse=True)
    larger_number = "".join(list_of_numbers)
    return larger_number


def read_input() -> List[str]:
    _ = input()
    list_of_numbers = input().split()
    return list_of_numbers


if __name__ == "__main__":
    list_of_numbers = read_input()
    print(make_larger_number(list_of_numbers))
