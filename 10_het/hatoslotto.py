#!/usr/bin/env python3

from typing import Tuple

LAST = 45 + 1


def nyero_szamok(osszeg, szorzat) -> Tuple[int]:
    for i in range(1, LAST + 1):
        for j in range(i + 1, LAST + 1):
            for k in range(j + 1, LAST + 1):
                for l in range(k + 1, LAST + 1):
                    for m in range(l + 1, LAST + 1):
                        for n in range(m + 1, LAST + 1):
                            if ((i + j + k + l + m + n) == osszeg and (i * j * k * l * m * n) == szorzat):
                                return (i, j, k, l, m, n)


def main():
    result = nyero_szamok(90, 996300)
    print(result)


if __name__ == "__main__":
    main()