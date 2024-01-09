#!/usr/bin/env python3

import re

INPUT = "naprendszer.txt"


def is_correct_line(szo: str) -> bool:
    n = re.search(r"j.*.*s.*u.*n", szo)
    if n:
        return True
    else:
        return False


def main() -> None:
    with open(INPUT) as f:
        for line in f:
            szo = line.split(",")[0]
            if is_correct_line(szo):
                print(szo)


if __name__ == "__main__":
    main()
