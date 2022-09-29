from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    short_alphabet = set(shorter)
    long_alphabet = set(longer)
    dif = long_alphabet.difference(short_alphabet)
    if dif:
        return "".join(dif)
    for letter in short_alphabet:
        if shorter.count(letter) != longer.count(letter):
            return letter


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


if __name__ == "__main__":
    shorter, longer = read_input()
    print(get_excessive_letter(shorter, longer))
