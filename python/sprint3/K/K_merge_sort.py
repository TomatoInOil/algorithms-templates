from typing import List


def merge(arr: List, left: int, mid: int, right: int) -> List:
    l_arr = arr[left:mid]
    r_arr = arr[mid:right]
    l_index, r_index, k_index = 0, 0, left
    while l_index < len(l_arr) and r_index < len(r_arr):
        if l_arr[l_index] <= r_arr[r_index]:
            arr[k_index] = l_arr[l_index]
            l_index += 1
        else:
            arr[k_index] = r_arr[r_index]
            r_index += 1
        k_index += 1
    while l_index < len(l_arr):
        arr[k_index] = l_arr[l_index]
        l_index += 1
        k_index += 1
    while r_index < len(r_arr):
        arr[k_index] = r_arr[r_index]
        r_index += 1
        k_index += 1
    return arr[left:right]


def merge_sort(arr: List, left: int, right: int) -> None:
    mid = (left + right) // 2
    if right - left <= 2:
        merge(arr, left, mid, right)
        return
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
