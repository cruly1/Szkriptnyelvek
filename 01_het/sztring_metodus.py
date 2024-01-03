#!/usr/bin/env python3


# a szkript nagybetűsíti a felhasználó nevét, ha véletlenül kisbetűvel adta volna meg
def main():
    s = input("Add meg a neved: ").capitalize()
    print(f"Hello {s}!")


if __name__ == "__main__":
    main()
