#!/usr/bin/env python3

from typing import List


def print_pages(s) -> List[int]:
    li = s.split(",")
    parts = []

    for e in li:
        if "-" in e:
            tmp = e.split("-")
            start = int(tmp[0])
            end = int(tmp[1]) + 1
            parts += (e for e in (range(start, end)))
        else:
            parts.append(int(e))

    return parts


def main():
    s = input("Adja meg a kinyomtatni kivant oldalakat a kovetkezo modon (1-4,7,9,11-15): ")
    res = print_pages(s)
    print(res)


if __name__ == "__main__":
    main()
