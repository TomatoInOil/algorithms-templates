def bracket_generator(
    number_of_pairs: int,
    prefix: str = "",
    opened: int = 0,
    closed: int = 0,
) -> None:
    if opened + closed == 2 * number_of_pairs:
        print(prefix)
    if opened < number_of_pairs:
        bracket_generator(number_of_pairs, prefix + "(", opened + 1, closed)
    if closed < opened:
        bracket_generator(number_of_pairs, prefix + ")", opened, closed + 1)


if __name__ == "__main__":
    bracket_generator(int(input()))
