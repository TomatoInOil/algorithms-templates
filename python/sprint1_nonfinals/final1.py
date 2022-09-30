from typing import List, Tuple


def get_distances_to_empty_plot(n: int, house_numbers: List[int]) -> List[int]:
    indexes_of_zeros = []
    for index, house in enumerate(house_numbers):
        if house == 0:
            indexes_of_zeros.append(index)
    for i in range(len(indexes_of_zeros) - 1):
        if indexes_of_zeros[i + 1] - indexes_of_zeros[i] > 1:
            left = indexes_of_zeros[i] + 1
            right = indexes_of_zeros[i + 1] - 1
            current_distance = 1
            while left <= right:
                house_numbers[left] = house_numbers[right] = current_distance
                current_distance += 1
                left += 1
                right -= 1
    if indexes_of_zeros[0] != 0:
        current_distance = 1
        right = indexes_of_zeros[0] - 1
        while right >= 0:
            house_numbers[right] = current_distance
            current_distance += 1
            right -= 1
    if indexes_of_zeros[-1] != n - 1:
        current_distance = 1
        left = indexes_of_zeros[-1] + 1
        while left <= n - 1:
            house_numbers[left] = current_distance
            current_distance += 1
            left += 1
    return house_numbers


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    house_numbers = list(map(int, input().split()))
    return n, house_numbers


def main():
    n, house_numbers = read_input()
    print(
        " ".join(list(map(str, get_distances_to_empty_plot(n, house_numbers))))
    )


if __name__ == "__main__":
    main()
