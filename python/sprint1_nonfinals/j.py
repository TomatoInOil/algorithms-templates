from typing import List


def factorize(number: int) -> List[int]:
    root_of_number = int(number ** (0.5) + 2)
    is_prime = [False, True] * int(root_of_number / 2 + 1)
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(root_of_number ** (0.5) + 2), 2):
        if is_prime[i]:
            for x in range(i * i, root_of_number, 2 * i):
                is_prime[x] = False
    primes = [p for p in range(root_of_number) if is_prime[p]]
    result = []
    for p in primes:
        while number % p == 0:
            result.append(p)
            number //= p
    if number != 1:
        result.append(number)
    return result


if __name__ == "__main__":
    result = factorize(int(input()))
    print(" ".join(map(str, result)))
