#!/usr/bin/env python3

INPUT = "string1.py"
OUTPUT = "string1_clean.py"


def main():
    with open(INPUT, "r") as f1, open(OUTPUT, "w") as f2:
        for line in f1:
            if (not line.strip().startswith("#")) and (not line == "\n"):
                line = line.rstrip("\n")
                print(line, file=f2)


if __name__ == "__main__":
    main()
