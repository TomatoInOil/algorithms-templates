from typing import List, Tuple


def get_maximum_number_of_points(k: int, keyboard: List[str]) -> int:
    count_of_keys = [keyboard.count(str(i)) for i in range(1, 10)]
    score = 0
    for count in count_of_keys:
        if count <= k and count != 0:
            score += 1
    return score


def read_input() -> Tuple[int, List[str]]:
    k = 2 * int(input())
    keyboard = []
    for _ in range(4):
        keyboard += list(input())
    return k, keyboard


def main():
    k, keyboard = read_input()
    print(get_maximum_number_of_points(k, keyboard))


if __name__ == "__main__":
    main()
