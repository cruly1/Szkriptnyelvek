#!/usr/bin/env python3

INPUT = "input.txt"


def main():
    result = 0
    lines = []
    with open(INPUT, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            lines.append(line)

    for line in lines:
        if len(line.split()) == len(set(line.split())):
            result += 1

    print(result)


if __name__ == "__main__":
    main()
