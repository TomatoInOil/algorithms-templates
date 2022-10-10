def get_number_of_commits(i: int) -> int:
    """Возвращает число коммитов i-го стажера."""
    if i == 0 or i == 1:
        return 1
    return get_number_of_commits(i - 1) + get_number_of_commits(i - 2)


if __name__ == "__main__":
    i = int(input())
    print(get_number_of_commits(i))
