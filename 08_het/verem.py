#!/usr/bin/env python3


class Stack:
    def __init__(self):
        self.li = []

    def ures(self):
        return not self.li

    def betesz(self, value):
        self.li.append(value)

    def kivesz(self):
        if self.ures():
            return None

        return self.li.pop()

    def meret(self):
        return len(self.li)

    def __str__(self):
        return str(self.li).replace("]", "").replace(",", "")


def main():
    v = Stack()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)


if __name__ == "__main__":
    main()
