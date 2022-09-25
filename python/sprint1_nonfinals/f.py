import string


def is_palindrome(line: str) -> bool:
    table = line.maketrans("", "", string.punctuation + string.whitespace)
    line = line.translate(table).lower()
    if line == line[::-1]:
        return True
    return False


if __name__ == "__main__":
    print(is_palindrome(input().strip()))
