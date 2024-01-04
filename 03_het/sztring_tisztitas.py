#!/usr/bin/env python3


def string_cleaner(s):
    return "".join(s.split())


def main():
    ip1 = string_cleaner("192.20.246.138:\n 6666")
    ip2 = string_cleaner("206.130.99.82:\n8080")

    print(ip1)
    print(ip2)


if __name__ == "__main__":
    main()
