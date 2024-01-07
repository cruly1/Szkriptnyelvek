#!/usr/bin/env python3

BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def bracket(s):
    stack = []
    for c in s:
        if c in BRACKETS.keys():
            stack.append(BRACKETS[c])
        elif c in BRACKETS.values():
            if not stack or c != stack.pop():
                return False

    return not stack


def main():
    print(bracket("((5+3)*2+1)") == True)
    print(bracket("{[(3+1)+2]+}") == True)
    print(bracket("(3+{1-1)}") == False)
    print(bracket("[1+1]+(2*2)-{3/3}") == True)
    print(bracket("(({[(((1)-2)+3)-3]/3}-3)") == False)


if __name__ == "__main__":
    main()
