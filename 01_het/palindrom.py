#!/usr/bin/env python3


def is_palindrome(s):
    return s == s[::-1]


def main():
    s = "gorog"
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
