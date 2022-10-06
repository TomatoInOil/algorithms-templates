BRACKET_PAIRS = {
    "(": ")",
    "[": "]",
    "{": "}",
}


def is_correct_bracket_seq(sequence: str) -> bool:
    if sequence == "":
        return True
    open_bracket = BRACKET_PAIRS.keys()
    closed_bracket = BRACKET_PAIRS.values()
    expected_brackets = []
    for char in sequence:
        if char in open_bracket:
            expected_brackets.append(BRACKET_PAIRS[char])
            continue
        if char in closed_bracket:
            if not expected_brackets:
                return False
            if char == expected_brackets[-1]:
                expected_brackets.pop()
                continue
            return False
    if expected_brackets:
        return False
    return True


if __name__ == "__main__":
    sequence = input()
    print(is_correct_bracket_seq(sequence))
