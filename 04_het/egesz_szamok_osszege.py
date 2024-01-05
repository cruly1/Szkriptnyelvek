#!/usr/bin/env python3


def count(n):
    return sum([int(digit) for digit in str(n)])


def main():
    res = 0
    for i in range(1, 100+1):
        res += count(i)

    print(res)


if __name__ == "__main__":
    main()
