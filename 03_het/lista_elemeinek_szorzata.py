#!/usr/bin/env python3


def prod(li):
    res = 1

    for n in li:
        res *= n

    return res


def main():
    # li = []
    li = [1, 2, 3, 4, 5]
    res = prod(li)
    print(res)


if __name__ == "__main__":
    main()
