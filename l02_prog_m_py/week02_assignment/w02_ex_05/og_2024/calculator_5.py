# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - calculator_5.py
#
# Veckouppgift 2
# Vecka 3, 13/1
# 5 Miniräknare
#####################################################################


middle = False
same_int = 0


# Ask for and save an integer in a variable
# Throw ValueError if incorrect input (not an integer), then try again
def userint_input(info_text):
    # noqa
    while True:
        try:
            user_int = int(input(info_text))
            return user_int
            break
        except ValueError:
            print("\nNot an integer, please try again!\n")


print("\nYou will be asked to input three integers, one at the time.")
input("Press Enter to continue.\n")

num1 = userint_input(("Please enter your first integer, then press enter: "))
num2 = userint_input(("Please enter your second integer, then press enter: "))
num3 = userint_input(("Please enter your third integer, then press enter: "))

sum_three = num1 + num2 + num3

print("\n1: The sum of your three integers is:" , sum_three)
input("Press Enter to continue.\n")


# Use "if/elif/else" to find the greatest integer of the three
if ((num1 >= num2) and (num1 >= num3)):
    max_int = num1
elif ((num2 >= num1) and (num2 >= num3)):
    max_int = num2
else:
    max_int = num3

print("\n2: The greatest integer of those entered is:" , max_int)
input("Press Enter to continue.\n")


# Check if there are any identical integers,
# also handle if "middle" is impossible or not
if (num1 == num2):
    middle = False
    if (num1 == num3):
        same_int = 3
    else:
        same_int = 2
elif (num1 == num3):
    middle = False
    same_int = 2
elif (num2 == num3):
    middle = False
    same_int = 2
else:
    middle = True
    same_int = 1


# Handle parts 3 and 4 printouts
# Including checks for middle, if applicable
if same_int in (2, 3):
    print("\n3: There are identical numbers," , same_int , "of them!")
    print("4: There is no middle number!")
    input("\nPress Enter to finish!")
elif middle:
    print("\n3: There are no identical numbers!")
    if ((num2 < num1 and num1 < num3) or (num3 < num1 and num1 < num2)):
        mid_int = num1
    elif ((num1 < num2 and num2 < num3) or (num3 < num2 and num2 < num1)):
        mid_int = num2
    else:
        mid_int = num3
    print("4: The middle number is" , mid_int)
    input("\nPress Enter to finish!")
