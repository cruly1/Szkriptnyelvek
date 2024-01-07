#!/usr/bin/env python3


class Queue:
    def __init__(self):
        self.li = []

    def ures(self):
        return not self.li

    def betesz(self, value):
        self.li.append(value)

    def kivesz(self):
        if self.ures():
            return None

        return self.li.pop(0)

    def meret(self):
        return len(self.li)

    def __str__(self):
        return "< " + str(self.li).replace("[", "").replace("]", "").replace(",", "") + " >"


def main():
    q = Queue()
    print(q)
    print(q.ures())
    q.betesz(1)
    q.betesz(4)
    q.betesz(5)
    print(q)
    print(q.meret())
    print(q.ures())
    x = q.kivesz()
    print(x)
    print(q)
    q.kivesz()
    q.kivesz()
    x = q.kivesz()
    print(x)


if __name__ == "__main__":
    main()
