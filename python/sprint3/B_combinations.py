from typing import List


dictionary_of_keys = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def get_all_letter_combinations_from_numbers(
    pressed_keys: List[str], string: str = ""
) -> str:
    """Перебирает все комбинации букв, которые могли быть набраны."""
    combinations = []
    number_of_clicks = len(pressed_keys)
    if number_of_clicks == 0:
        return string
    key = pressed_keys.pop(0)
    letters = dictionary_of_keys[key]
    for letter in letters:
        combinations.append(
            get_all_letter_combinations_from_numbers(
                pressed_keys.copy(), string + letter
            )
        )
    return " ".join(combinations)


if __name__ == "__main__":
    print(get_all_letter_combinations_from_numbers(list(input())))
