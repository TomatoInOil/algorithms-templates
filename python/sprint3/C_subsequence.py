def is_subsequence(first_seq: str, second_seq: str) -> bool:
    """Является ли первая последовательно подпоследовательностью второй."""
    last_f_index, last_s_index = len(first_seq) - 1, len(second_seq) - 1
    f_index, s_index = 0, 0
    while f_index <= last_f_index and s_index <= last_s_index:
        if first_seq[f_index] == second_seq[s_index]:
            f_index += 1
            s_index += 1
            continue
        if s_index == last_s_index:
            return False
        s_index += 1
    return f_index == last_f_index + 1


if __name__ == "__main__":
    first_seq = input()
    second_seq = input()
    print(is_subsequence(first_seq, second_seq))
