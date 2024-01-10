#!/usr/bin/env python3

import json

INPUT = "primes.json"


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def main():
    with open(INPUT) as f:
        d = json.load(f)

    result = [i for i in d["primes"] if is_palindrome(i)]
    print(result)


if __name__ == "__main__":
    main()
