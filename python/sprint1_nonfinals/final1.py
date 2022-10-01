from typing import List, Tuple


def get_distances_to_empty_plot(
    street_length: int, house_numbers: List[str]
) -> List[str]:
    indexes_of_zeros = []
    for index, house in enumerate(house_numbers):
        if house == "0":
            indexes_of_zeros.append(index)
    for index in range(len(indexes_of_zeros) - 1):
        if indexes_of_zeros[index + 1] - indexes_of_zeros[index] > 1:
            left = indexes_of_zeros[index] + 1
            right = indexes_of_zeros[index + 1] - 1
            current_distance = 1
            while left <= right:
                house_numbers[left] = house_numbers[right] = str(
                    current_distance
                )
                current_distance += 1
                left += 1
                right -= 1
    if indexes_of_zeros[0] != 0:
        current_distance = 1
        right = indexes_of_zeros[0] - 1
        while right >= 0:
            house_numbers[right] = str(current_distance)
            current_distance += 1
            right -= 1
    if indexes_of_zeros[-1] != street_length - 1:
        current_distance = 1
        left = indexes_of_zeros[-1] + 1
        while left <= street_length - 1:
            house_numbers[left] = str(current_distance)
            current_distance += 1
            left += 1
    return house_numbers


def read_input() -> Tuple[int, List[str]]:
    street_length = int(input())
    house_numbers = input().split()
    return street_length, house_numbers


if __name__ == "__main__":
    street_length, house_numbers = read_input()
    print(" ".join(get_distances_to_empty_plot(street_length, house_numbers)))
