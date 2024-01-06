#!/usr/bin/env python3


def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    parts = []
    for c in text:
        if c in chars:
            parts.append(c)
    return "".join(parts)


def main():
    res1 = valid("Barking!")
    res2 = valid("KL754", "0123456789")
    res3 = valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

    print(res1)
    print(res2)
    print(res3)


if __name__ == "__main__":
    main()
