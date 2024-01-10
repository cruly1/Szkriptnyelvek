#!/usr/bin/env python3

import json

from math import sqrt
from typing import List

MAX = 10_000_000
INPUT = "primes.json"


def get_primes(n) -> List[int]:
    lst = [True]*n
    res = []
    for i in range(2,int(sqrt(n))+1):
        if (lst[i]):
            for j in range(i*i, n, i):
                lst[j] = False
    for i in range(2,n):
        if lst[i]:
            res.append(i)

    return res


def main():
    li = get_primes(MAX)
    d = {"primes": li}

    with open(INPUT, "w") as f:
        json.dump(d, f, indent=4)


if __name__ == "__main__":
    main()
