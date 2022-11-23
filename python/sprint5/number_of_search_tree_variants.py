from typing import List

LOCAL_TESTING = False


def get_number_of_search_tree_variants(number_of_nodes: int) -> int:
    """Возвращает сколько может быть различных деревьев поиска,
    содержащих в своих узлах все уникальные числа от 1 до number_of_nodes"""
    list_of_numbers = list(range(1, number_of_nodes + 1))
    result = composing_trees(list_of_numbers)
    return result


def composing_trees(list_of_numbers: List[int]):
    """Возвращает количество разных деревьев поиска из входного списка."""
    if len(list_of_numbers) == 2:
        return 2
    if len(list_of_numbers) == 0:
        return 1
    result = 0
    for index in range(len(list_of_numbers)):
        if index == 1:
            if index == len(list_of_numbers) - 2:
                result += 1
            else:
                result += composing_trees(
                    list_of_numbers[index + 1 : len(list_of_numbers)]
                )
        elif index == len(list_of_numbers) - 2:
            result += composing_trees(list_of_numbers[0:index])
        else:
            left = composing_trees(list_of_numbers[0:index])
            right = composing_trees(
                list_of_numbers[index + 1 : len(list_of_numbers)]
            )
            result += left * right
    return result


if __name__ == "__main__":
    if LOCAL_TESTING:
        assert get_number_of_search_tree_variants(2) == 2
        assert get_number_of_search_tree_variants(3) == 5
        assert get_number_of_search_tree_variants(4) == 14
        assert get_number_of_search_tree_variants(5) == 42
        assert get_number_of_search_tree_variants(6) == 132
        assert get_number_of_search_tree_variants(7) == 429
        assert get_number_of_search_tree_variants(8) == 1430

    else:
        number_of_nodes = int(input())
        print(get_number_of_search_tree_variants(number_of_nodes))
