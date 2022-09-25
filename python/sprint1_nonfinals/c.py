from typing import List, Tuple


def get_neighbours(
    n: int, m: int, matrix: List[List[int]], row: int, col: int
) -> List[int]:
    result = []
    if col != m - 1:
        result.append(matrix[row][col + 1])
    if col != 0:
        result.append(matrix[row][col - 1])
    if row != n - 1:
        result.append(matrix[row + 1][col])
    if row != 0:
        result.append(matrix[row - 1][col])
    result.sort()
    return result


def read_input() -> Tuple[int, int, List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return n, m, matrix, row, col


if __name__ == "__main__":
    n, m, matrix, row, col = read_input()
    print(" ".join(map(str, get_neighbours(n, m, matrix, row, col))))
