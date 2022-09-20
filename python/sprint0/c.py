from typing import List, Tuple


def moving_average(n: int, arr: List[int], window_size: int) -> List[float]:
    result = []
    current_sum = sum(arr[0:window_size])
    current_avg = current_sum / window_size
    result.append(current_avg)
    for index in range(1, n - window_size + 1):
        current_sum = (
            current_sum - arr[index - 1] + arr[index + window_size - 1]
        )
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return n, arr, window_size


if __name__ == "__main__":
    n, arr, window_size = read_input()
    print(" ".join(map(str, moving_average(n, arr, window_size))))
