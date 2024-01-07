#!/usr/bin/env python3


def is_anagramma(s1, s2):
    tmp1 = s1.lower()
    tmp2 = s2.lower()
    parts1 = [*tmp1].sort()
    parts2 = [*tmp2].sort()
    return parts1 == parts2


def main():
    s1 = "Clint Eastwood"
    s2 = "Old west action"
    print(is_anagramma(s1, s2))


if __name__ == "__main__":
    main()
