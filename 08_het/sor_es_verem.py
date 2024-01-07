#!/usr/bin/env python3


import verem


class Queue:
    def __init__(self):
        self.v1 = verem.Stack()
        self.v2 = verem.Stack()

    def ures(self):
        return not (self.v1.li or self.v2.li)

    def betesz(self, value):
        self.v1.betesz(value)

    def kivesz(self):
        if not self.meret():
            return None

        for e in reversed(self.v1.li):
            self.v2.betesz(e)
            self.v1.kivesz()

        res = self.v2.kivesz()

        for e in reversed(self.v2.li):
            self.v1.betesz(e)
            self.v2.kivesz()

        return res

    def meret(self):
        return self.v1.meret()

    def __str__(self):
        return "< " + str(self.v1).replace("[", "").replace("]", "") + " >"

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
