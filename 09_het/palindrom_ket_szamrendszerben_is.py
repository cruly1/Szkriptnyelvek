#!/usr/bin/env python3

NUM = 1000000


def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1]


def main():
    ctr = 0

    for i in range(NUM):
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            ctr += i

    print(ctr)


if __name__ == "__main__":
    main()
