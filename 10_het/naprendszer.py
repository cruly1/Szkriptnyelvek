#!/usr/bin/env python3

from typing import List

INPUT = "naprendszer.txt"


def is_correct_line(line) -> bool:
    line = line.lower()
    if not (("j" in line) and ("s" in line) and ("u" in line) and ("n" in line)):
        return False

    if not (line.find("j") < line.find("s")):
        return False

    if not (line.find("s") < line.find("u")):
        return False

    if not (line.find("u") < line.find("n")):
        return False

    return True


def get_words(lines) -> List[str]:
    li = [line for line in lines if is_correct_line(line)]
    return [s.split(",")[0] for s in li]


def main():
    try:
        with open(INPUT) as f:
            lines = [line.rstrip("\n") for line in f]

    except FileNotFoundError as e:
        print(e)
        exit(1)

    except:
        print("Unknown error")
        exit(2)

    results = get_words(lines)
    print("\n".join(results))


if __name__ == "__main__":
    main()
