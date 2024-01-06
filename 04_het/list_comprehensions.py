#!/usr/bin/env python3


def feladat1():
    words = ["auto", "villamos", "metro"]
    result = [word.upper() + "!" for word in words]
    print(f"{words} -> {result}")


def feladat2():
    words = ["aladar", "bela", "cecil"]
    result = [word.capitalize() for word in words]
    print(f"{words} -> {result}")


def feladat3():
    result = [0] * 10
    print(result)


def feladat4():
    nums = [i for i in range(1, 10+1)]
    result = [n * 2 for n in nums]
    print(f"{nums} -> {result}")

def feladat5():
    nums = [str(i) for i in range(1, 10+1)]
    result = [int(n) for n in nums]
    print(f"{nums} -> {result}")


def feladat6():
    s = "1234567"
    result = [int(c) for c in s]
    print(f"{s} -> {result}")


def feladat7():
    sentence = "The quick brown fox jumps over the lazy dog"
    result = [len(word) for word in sentence.split()]
    print(f"{sentence} -> {result}")


def feladat8():
    sentence = "python is an awesome language"
    result = [word[0] for word in sentence.split()]
    print(f"{sentence} -> {result}")


def feladat9():
    sentence = "The quick brown fox jumps over the lazy dog"
    result = [(word, len(word)) for word in sentence.split()]
    print(f"{sentence} -> {result}")


def feladat10():
    result = [i for i in range(10) if i%2==0]
    print(result)


def feladat11():
    result = [i*i for i in range(20) if i*i%2==0]
    print(result)


def feladat12():
    result = [i*i for i in range(20) if i*i%10==4]
    print(result)


def feladat13():
    result = "".join([chr(i) for i in range(65, 90+1)])
    print(result)


def feladat14():
    words = [" apple ", " banana ", " kiwi"]
    result = [word.strip() for word in words]
    print(f"{words} -> {result}")


def feladat15():
    nums = [1, 0, 1, 1, 0, 1, 0, 0]
    result = "".join([str(n) for n in nums])
    print(f"{nums} -> {result}")


def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()
    feladat9()
    feladat10()
    feladat11()
    feladat12()
    feladat13()
    feladat14()
    feladat15()


if __name__ == "__main__":
    main()
