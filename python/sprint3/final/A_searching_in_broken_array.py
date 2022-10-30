from typing import List


def broken_search(nums: List, target) -> int:
    last_index = len(nums) - 1
    left = 0
    right = last_index
    first_mid = (left + right) // 2
    prev_num = None
    while left <= right:
        mid = (left + right) // 2
        current_num = nums[mid]
        if current_num < target:
            left = mid + 1
            if prev_num:
                if prev_num[1] > current_num and search_for_larger:
                    left = (prev_num[0] + 1) % (last_index + 1)
                    right = mid - 1
            if left == last_index + 1:
                left = 0
                right = first_mid - 1
            search_for_larger = True
        elif target < current_num:
            right = mid - 1
            if prev_num:
                if prev_num[1] < current_num and not search_for_larger:
                    left = mid + 1
                    right = (prev_num[0] - 1) % (last_index + 1)
            if right == -1:
                left = first_mid + 1
                right = last_index
            search_for_larger = False
        else:
            return mid
        prev_num = (mid, current_num)
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 1]


if __name__ == "__main__":
    test()
