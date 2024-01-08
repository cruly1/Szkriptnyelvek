#!/usr/bin/env python3

CELL_COUNT = 600


def main():
    cells = [True for i in range(CELL_COUNT + 1)]

    for i in range(2, CELL_COUNT + 1):
        for j in range(i, CELL_COUNT + 1, i):
            cells[j] = not cells[j]


    opened_cells = [str(index) for index, value in enumerate(cells[1:], start=1) if value]
    print("".join(opened_cells))


if __name__ == "__main__":
    main()
