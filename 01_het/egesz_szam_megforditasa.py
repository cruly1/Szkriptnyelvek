#!/usr/bin/env python3


def reverse(num):
    return int(str(num)[::-1])


def main():
    num1 = 1977
    num2 = 12568
    res1 = reverse(num1)
    res2 = reverse(num2)
    print(res1)
    print(res2)


if __name__ == "__main__":
    main()
