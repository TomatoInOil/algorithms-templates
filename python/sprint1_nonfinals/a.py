def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    return a * x * x + b * x + c


if __name__ == "__main__":
    a, x, b, c = map(int, input().strip().split())
    print(evaluate_function(a, b, c, x))
