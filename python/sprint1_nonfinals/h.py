from typing import Tuple, List


def get_sum(first_number: List[int], second_number: List[int]) -> str:
    first_number.reverse()
    second_number.reverse()
    if len(first_number) > len(second_number):
        result = process_of_addition(
            larger_number=first_number, smaller_number=second_number
        )
    else:
        result = process_of_addition(
            larger_number=second_number, smaller_number=first_number
        )
    return "".join(result)


def process_of_addition(
    larger_number: List[int], smaller_number: List[int]
) -> List[str]:
    result = []
    carry = 0
    for i in range(len(larger_number)):
        if i < len(smaller_number):
            interim_sum = larger_number[i] + smaller_number[i] + carry
        else:
            interim_sum = larger_number[i] + carry
        if interim_sum % 2 == 0:
            if interim_sum:
                carry = 1
                result.append("0")
            else:
                carry = 0
                result.append("0")
        else:
            if interim_sum == 3:
                carry = 1
                result.append("1")
            else:
                carry = 0
                result.append("1")
    if carry:
        result.append("1")
    result.reverse()
    return result


def read_input() -> Tuple[List[int], List[int]]:
    first_number = [int(char) for char in input().strip()]
    second_number = [int(char) for char in input().strip()]
    return first_number, second_number


if __name__ == "__main__":
    first_number, second_number = read_input()
    print(get_sum(first_number, second_number))
