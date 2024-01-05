#!/usr/bin/env python3


def diamond(h):
    for i in range(1, h, 2):
        print(" " * (h // 2 - i // 2), "*" * i)
    for i in range(h, 0, -2):
        print(" " * (h // 2 - i // 2), "*" * i)


def main():
    m = int(input("A gyémánt magassága: "))

    if m % 2 == 0:
        print("Páros szám nem elfogadott!")
        exit(1)

    diamond(m)


if __name__ == '__main__':
    main()
