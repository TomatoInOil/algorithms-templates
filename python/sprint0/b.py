from typing import List, Tuple


def zipper(n: int, first_list: List[str], second_list: List[str]) -> List[str]:
    result = []
    for index in range(0, n):
        result.append(first_list[index])
        result.append(second_list[index])
    return result


def read_input() -> Tuple[int, List[str], List[str]]:
    n = int(input())
    first_list = input().strip().split()
    second_list = input().strip().split()
    return n, first_list, second_list


if __name__ == "__main__":
    n, first_list, second_list = read_input()
    print(" ".join(zipper(n, first_list, second_list)))
