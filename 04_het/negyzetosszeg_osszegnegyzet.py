#!/usr/bin/env python3


N = 100

def negyzet_osszeg():
    res = 0
    for i in range(1, N+1):
        res += i ** 2

    return res


def osszeg_negyzet():
    return(sum(range(1, N+1)) ** 2)


def main():
    res = osszeg_negyzet() - negyzet_osszeg()
    print(res)


if __name__ == "__main__":
    main()
