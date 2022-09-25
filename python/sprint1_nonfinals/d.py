from typing import List, Tuple


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    if n == 1:
        return 1
    count = 0
    step_back = temperatures[0] - temperatures[1]
    if step_back > 0:
        count += 1
    for i in range(1, n - 1):
        step_forward = temperatures[i + 1] - temperatures[i]
        if step_back < 0 and step_forward < 0:
            count += 1
        step_back = -step_forward
    if step_back < 0:
        count += 1
    return count


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures


if __name__ == "__main__":
    n, temperatures = read_input()
    print(get_weather_randomness(n, temperatures))
