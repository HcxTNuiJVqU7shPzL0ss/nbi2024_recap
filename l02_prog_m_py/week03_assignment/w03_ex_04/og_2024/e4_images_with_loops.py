# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e4_images_with_loops.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 4 Figurer med loopar
#####################################################################


"""
Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
"""


print('\nExercise 4')


# Image 'a'
input("\nPress enter to continue")
print('\n...................."4.a"....................\n')
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)


# Image 'b'
input("\nPress enter to continue")
print('\n...................."4.b"....................\n')
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)


# Image 'c'
input("\nPress enter to continue")
print('\n...................."4.c"....................\n')
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 2 < x < 6:
            s += "#"
        else:
            s += "."
    print(s)


# Image 'd'
input("\nPress enter to continue")
print('\n...................."4.d"....................\n')
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


# Image 'e'
input("\nPress enter to continue")
print('\n...................."4.e"....................\n')
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


# Image 'f'
input("\nPress enter to continue")
print('\n...................."4.f"....................\n')
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


# Image 'g'
input("\nPress enter to continue")
print('\n...................."4.g"....................\n')
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if (x % 2) != 0:
            s += "#"
        else:
            s += "."
    print(s)


# Image 'h'
input("\nPress enter to continue")
print('\n...................."4.h"....................\n')
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


# Image 'i'
input("\nPress enter to continue")
print('\n...................."4.i"....................\n')
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


# Image 'j'
input("\nPress enter to continue")
print('\n...................."4.j"....................\n')
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


# End program
input("\nPress enter to finish!")
