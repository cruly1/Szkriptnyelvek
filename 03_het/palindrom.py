#!/usr/bin/env python3


def is_palindrome(s):
    i = 0
    while i < len(s) / 2:
        if s[i] != s[-i-1]:
            return False
        i += 1

    return True


def main():
    s = "gorog"
    # s = "nempalindrom"
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
