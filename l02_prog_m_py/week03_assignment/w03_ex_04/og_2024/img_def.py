# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - img_def.py
#
# Function definition to use for exercise 4 == "different"
#####################################################################


def img_a(info_string):
    # noqa
    # Image 'a'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 1:
                s += "#"
            else:
                s += "."
        print(s)


def img_b(info_string):
    # noqa
    # Image 'b'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)


def img_c(info_string):
    # noqa
    # Image 'c'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if 2 < x < 6:
                s += "#"
            else:
                s += "."
        print(s)


def img_d(info_string):
    # noqa
    # Image 'd'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y != 3:
                if x == 3:
                    s += "#"
                else:
                    s += "."
            else:
                s += "#"
        print(s)


def img_e(info_string):
    # noqa
    # Image 'e'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 1:
                if 4 < x < 7:
                    s += "#"
                else:
                    s += "."
            elif y == 2:
                if x == 5:
                    s += "#"
                else:
                    s += "."
            elif y == 3:
                if 3 < x < 6:
                    s += "#"
                else:
                    s += "."
            elif y == 4:
                if x == 3 or x == 5:
                    s += "#"
                else:
                    s += "."
            elif y == 5:
                if x == 2 or x == 5:
                    s += "#"
                else:
                    s += "."
            elif y == 6:
                if x == 1 or x == 5:
                    s += "#"
                else:
                    s += "."
        print(s)


def img_f(info_string):
    # noqa
    # Image 'f'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 1 or y == 6:
                if x == 1 or x == 6:
                    s += "#"
                else:
                    s += "."
            elif y == 2 or y == 5:
                if x == 2 or x == 5:
                    s += "#"
                else:
                    s += "."
            elif y == 3 or y == 4:
                if x == 3 or x == 4:
                    s += "#"
                else:
                    s += "."
        print(s)


def img_g(info_string):
    # noqa
    # Image 'g'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if (x % 2) != 0:
                s += "#"
            else:
                s += "."
        print(s)

def img_h(info_string):
    # noqa
    # Image 'h'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 1 or y == 6:
                s += "."
            elif y == 3 or y == 4:
                if x == 2 or x == 7:
                    s += "#"
                else:
                    s += "."
            else:
                if 1 < x < 8:
                    s += "#"
                else:
                    s += "."
        print(s)


def img_i(info_string):
    # noqa
    # Image 'i'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 1 or y == 4:
                if x in (1, 4, 7):
                    s += "."
                elif x in (2, 5, 8):
                    s += "#"
                else:
                    s += "0"
            elif y == 2 or y == 5:
                if x in (2, 5, 8):
                    s += "."
                elif x in (3, 6):
                    s += "#"
                else:
                    s += "0"
            else:
                if x in (3, 6):
                    s += "."
                elif x in (1, 4, 7):
                    s += "#"
                else:
                    s += "0"
        print(s)


def img_j(info_string):
    # noqa
    # Image 'j'
    input("\nPress enter to continue")
    print(info_string)
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y in (1, 2, 3):
                if x in (3, 6):
                    s += "#"
                else:
                    s += "."
            elif y == 4:
                s += "."
            elif y == 5:
                if (x % 2) != 0:
                    s += "."
                else:
                    s += "#"
            else:
                if (x % 2) == 0:
                    s += "."
                else:
                    s += "#"
        print(s)
