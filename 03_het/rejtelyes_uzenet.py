#!/usr/bin/env python3


TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def decode(t1, t2):
    res = ""
    for c in TEXT:
        if c in t1:
            index = t1.find(c)
            res += t2[index]
        else:
            res += c

    return res


def main():
    t1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    t2 = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"

    result = decode(t1, t2)
    print(result)


if __name__ == "__main__":
    main()
