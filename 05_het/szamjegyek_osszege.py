#!/usr/bin/env python3

NUM = 2 ** 1000


def main():
    s = str(NUM)
    result = sum([int(c) for c in s])
    print(result)


if __name__ == "__main__":
    main()
