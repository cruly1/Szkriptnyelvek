#!/usr/bin/env python3

INPUT = "input.txt"


def checksum(line):
    tmp = line.split()
    parts = [int(n) for n in tmp]
    return max(parts) - min(parts)


def main():
    lines = []
    with open(INPUT, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            lines.append(checksum(line))

    result = sum(lines)

    print(result)


if __name__ == "__main__":
    main()
