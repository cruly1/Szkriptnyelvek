#!/usr/bin/env python3

import sys


def main():
    parts = []
    for i in range(97, 122+1):
        parts.append(chr(i))
    res = "".join(parts)

    if sys.argv[0].endswith("a-z.py"):
        print(res)
    elif sys.argv[0].endswith("z-a.py"):
        print(res[::-1])


if __name__ == "__main__":
    main()
