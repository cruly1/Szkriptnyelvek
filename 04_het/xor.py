#!/usr/bin/env python3


def xor(str1, str2):
    if (bool(str1) != bool(str2)):
        return True

    return False


def main():
    str1 = "Python"
    str2 = None
    res = xor(str1, str2)
    print(res)


if __name__ == "__main__":
    main()
