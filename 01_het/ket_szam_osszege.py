#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) < 3:
        print("Hiba! Legalabb ket parancssori argumentumot adj meg!")
        exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(num1 + num2)


if __name__ == "__main__":
    main()
