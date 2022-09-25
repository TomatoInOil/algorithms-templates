def get_longest_word(line: str) -> str:
    words = line.split()
    words.reverse()
    word_lengths = sorted(
        {len(word): word for word in words}.items(), reverse=True
    )
    return word_lengths[0]


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result[1])
    print(result[0])


if __name__ == "__main__":
    print_result(get_longest_word(read_input()))
