def to_binary(number: int) -> str:
    if number == 0:
        return "0"
    remainders = []
    while number != 0:
        remainders.append(str(number % 2))
        number //= 2
    remainders.reverse()
    return "".join(remainders)


def read_input() -> int:
    return int(input().strip())


if __name__ == "__main__":
    print(to_binary(read_input()))
