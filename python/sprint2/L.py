def last_digits_of_fibonacci_numbers(i: int, k: int):
    """Возвращает k последних цифр i-го числа Фибоначчи."""
    if i == 0 or i == 1:
        return 1
    divisor = 10**k
    cache = [1, 1]
    for _ in range(i - 1):
        next_number = (cache.pop(0) + cache[0]) % divisor
        cache.append(next_number)
    return cache[1]


if __name__ == "__main__":
    i, k = tuple(map(int, input().split()))
    print(last_digits_of_fibonacci_numbers(i, k))
