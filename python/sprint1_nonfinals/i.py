def is_power_of_four(number: int) -> bool:
    remainder = 0
    if number == 0:
        return False
    while number != 1 or remainder != 0:
        remainder = number % 4
        if remainder != 0:
            return False
        number //= 4
    return True


if __name__ == "__main__":
    print(is_power_of_four(int(input())))
