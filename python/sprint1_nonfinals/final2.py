from typing import List, Tuple


def get_maximum_number_of_points(
    number_of_clicks: int, keyboard: List[str]
) -> int:
    count_of_keys = [keyboard.count(str(key)) for key in range(1, 10)]
    score = 0
    for count in count_of_keys:
        if count <= number_of_clicks and count != 0:
            score += 1
    return score


def read_input() -> Tuple[int, List[str]]:
    number_of_clicks = 2 * int(input())
    keyboard = []
    for _ in range(4):
        keyboard += list(input())
    return number_of_clicks, keyboard


if __name__ == "__main__":
    number_of_clicks, keyboard = read_input()
    print(get_maximum_number_of_points(number_of_clicks, keyboard))
