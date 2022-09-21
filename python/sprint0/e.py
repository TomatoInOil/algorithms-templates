from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    seen = set()
    for elem in arr:
        current_difference = target_sum - elem
        if current_difference in seen:
            return current_difference, elem
        seen.add(elem)
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    arr, target_sum = read_input()
    print_result(two_sum(arr, target_sum))
