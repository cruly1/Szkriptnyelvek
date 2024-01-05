#!/usr/bin/env python3


MELY_MGHK = "aáoóuú"
MAGAS_MGHK = "eéiíöőüű"

def hangrend(word):
    mely = False
    magas = False

    for c in word:
        if c in MELY_MGHK:
            mely = True
        if c in MAGAS_MGHK:
            magas = True

    if mely and magas:
        return 0
    if mely:
        return 1
    if magas:
        return 2

    return 3


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffff"]

    for e in words:
        res = hangrend(e)
        if res == 0:
            print(f"{e} -> vegyes")
        if res == 1:
            print(f"{e} -> mely")
        if res == 2:
            print(f"{e} -> magas")
        if res == 3:
            print(f"{e} -> semmilyen")


if __name__ == "__main__":
    main()
