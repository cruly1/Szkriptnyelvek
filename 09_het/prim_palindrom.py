#!/usr/bin/env python3


def is_prime(n) -> bool:
    if n<2:
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True


def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1]


def is_prime_and_palindrome(n) -> int:
    res = n
    while True:
        if is_prime(res) and is_palindrome(res):
            return res
        res += 1


def main():
    n = int(input("Kerlek adj meg egy egesz szamot: "))
    result = is_prime_and_palindrome(n)
    print(result)


if __name__ == "__main__":
    main()
