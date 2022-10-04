from typing import List, Tuple


def transposition(
    number_of_rows: int, number_of_columns: int, matrix: List[List[str]]
) -> List[List[str]]:
    """Транспонирование матрицы."""
    result_matrix = [[None] * number_of_rows for _ in range(number_of_columns)]
    for col in range(number_of_columns):
        for row in range(number_of_rows):
            result_matrix[col][row] = matrix[row][col]
    return result_matrix


def read_input() -> Tuple[int, int, List[List[str]]]:
    number_of_rows = int(input())
    number_of_columns = int(input())
    matrix = [input().split() for _ in range(number_of_rows)]
    return number_of_rows, number_of_columns, matrix


if __name__ == "__main__":
    number_of_rows, number_of_columns, matrix = read_input()
    result_matrix = transposition(number_of_rows, number_of_columns, matrix)
    print("\n".join([" ".join(row) for row in result_matrix]))
