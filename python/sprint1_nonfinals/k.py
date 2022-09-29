from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[str]:
    number_list.reverse()
    for index in range(len(number_list)):
        number_list[index] *= 10 ** (index)
    return list(str(sum(number_list) + k))


def read_input() -> Tuple[List[int], int]:
    _ = input()
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


if __name__ == "__main__":
    number_list, k = read_input()
    print(" ".join(get_sum(number_list, k)))
