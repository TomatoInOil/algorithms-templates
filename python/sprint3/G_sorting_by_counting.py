from typing import List


def sort_clothes_by_color(clothes: List[str]) -> str:
    """Сортирует одежду в гардеробе по цвету.
    Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2."""
    count_colors = {"0": 0, "1": 0, "2": 0}
    for elem in clothes:
        count_colors[elem] += 1
    sorted_clothes = []
    for color, count in count_colors.items():
        sorted_clothes += color * count
    return " ".join(sorted_clothes)


if __name__ == "__main__":
    _ = input()
    clothes = input().split()
    print(sort_clothes_by_color(clothes))
