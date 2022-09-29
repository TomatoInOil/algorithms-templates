from typing import List, Tuple
import string


def get_sum(number_list: int, k: int) -> List[str]:
    result = list(str(number_list + k))
    return result


def read_input() -> Tuple[int, int]:
    _ = input()
    number_list = input().strip()
    table = number_list.maketrans("", "", string.whitespace)
    number_list = int(number_list.translate(table))
    k = int(input())
    return number_list, k


if __name__ == "__main__":
    number_list, k = read_input()
    print(" ".join(get_sum(number_list, k)))
