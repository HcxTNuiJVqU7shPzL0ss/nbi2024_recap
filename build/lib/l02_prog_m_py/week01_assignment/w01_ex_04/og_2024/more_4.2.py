# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - more_4.2.py
#
# Programmering med Python, 20yhp
# Veckouppgift 1
# Vecka 2, 8/1
#
# 4 Fler övningar - Lite mer avancerad nivå
#
# "2"
# Skriv ett program som räknar ut längden på hypotenusan i
# en rätvinklig triangel.
# Användaren behöver skriva in längden på de två kortare sidorna.
#####################################################################


import math


print("\nThis is 4:2 == Calculate the length of the hypotenuse")
input("\nPress Enter to continue!")


# Ask for and save a number in a variable, for "side x"
# Throw ValueError if incorrect input (not int or float), then try again
# Negative numbers seen as positive
def triangle_side(side_no):
    # noqa: D103
    print("\nYou will be asked to input a side of a right triangle")
    while True:
        side = input("\nPlease input side " + str(side_no) + \
                     " length, then press enter: ")
        try:
            side_i = int(side)              # Check if int
            side_numeral = abs(side_i)      # Make sure positive
            return  side_numeral
            # break
        except ValueError:
            try:
                side_f = float(side)        # Check if float
                side_numeral = abs(side_f)  #Make sure positive
                return side_numeral
                # break
            except ValueError:              # Input not int or float
                print("Selected input not integer or float!")
                print("Please try again...")
                continue


side1_numeral = triangle_side(1)
side2_numeral = triangle_side(2)


input("\nPress Enter to continue!")


# Calculate the square of the hypotenuse
hyp_square = (side1_numeral * side1_numeral) + (side2_numeral * side2_numeral)

# Calculate the square root of the hypotenuse == the length
hyp_length = math.sqrt(hyp_square)
print("\nThe length of the hypotenuse is:" , hyp_length)

# Round to maximum 2 decimals
hyp_rounded = round(hyp_length, 2)
print("The length of the hypotenuse (rounded) is:" , hyp_rounded)
