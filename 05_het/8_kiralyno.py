#!/usr/bin/env python3

TABLE = {
        0: "| Q . . . . . . . |",
        1: "| . Q . . . . . . |",
        2: "| . . Q . . . . . |",
        3: "| . . . Q . . . . |",
        4: "| . . . . Q . . . |",
        5: "| . . . . . Q . . |",
        6: "| . . . . . . Q . |",
        7: "| . . . . . . . Q |",
    }


def eight_queens(li):
    tmp = sorted(li)
    print("+", " - " * 5, "+")

    for n in reversed(tmp):
        print(TABLE[li.index(n)])

    print("+", " - " * 5, "+")


def main():
    li = [7, 3, 0, 2, 5, 1, 6, 4]
    eight_queens(li)


if __name__ == "__main__":
    main()