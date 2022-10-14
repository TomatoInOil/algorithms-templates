from typing import List, Tuple


def get_day_of_purchase(
    list_of_savings: List[int],
    cost: int,
    left: int,
    right: int,
) -> int:
    """Получить день, когда Вася мог бы потратить cost денег."""
    mid = (right + left) // 2
    saved = list_of_savings[mid]
    if saved >= cost and (list_of_savings[mid - 1] < cost or mid == 0):
        return mid + 1
    if right <= left:
        return -1
    if cost > saved:
        return get_day_of_purchase(list_of_savings, cost, mid + 1, right)
    if cost <= saved:
        return get_day_of_purchase(list_of_savings, cost, left, mid)


def read_input() -> Tuple[int, List[int], int]:
    number_of_days = int(input())
    list_of_savings = list(map(int, input().split()))
    cost = int(input())
    return number_of_days, list_of_savings, cost


if __name__ == "__main__":
    number_of_days, list_of_savings, cost = read_input()
    day_of_one_bicycle = get_day_of_purchase(
        list_of_savings, cost, 0, number_of_days - 1
    )
    print(
        " ".join(
            (
                str(day_of_one_bicycle),
                str(
                    get_day_of_purchase(
                        list_of_savings,
                        2 * cost,
                        day_of_one_bicycle,
                        number_of_days - 1,
                    )
                ),
            )
        )
    )
