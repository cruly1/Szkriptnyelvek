#!/usr/bin/env python3

TEXT = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
""".strip()

d = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ö': 'o',
    'ő': 'o',
    'ú': 'u',
    'ü': 'u',
    'ű': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ö': 'O',
    'Ő': 'O',
    'Ú': 'U',
    'Ü': 'U',
    'Ű': 'U',
}


def main():
    parts = [d[c] if c in d else c for c in TEXT]
    result = "".join(parts)

    print(result)



if __name__ == "__main__":
    main()
