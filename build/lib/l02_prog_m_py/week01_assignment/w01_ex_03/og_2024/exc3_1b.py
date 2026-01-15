# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - exc3_1b.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper
# 1b
#####################################################################


# Import function, mainly to be able to rerun "1a"
# This is to be able to have 1a and 1b in separate files
from int_input_def import userint_input


# First need to (re)run "1a" to get the first integer
print("\nFirst input an integer as in 1a\n")
first_int = userint_input("Please type an integer, then press enter: ")


# --------------------------------------------
# 1b Fråga användaren efter ett annat heltal.
# Skriv ut summan av talen, alltså tal1 + tal2.
# Testa genom att hitta på två tal och räkna ut summan i huvudet.
# Kontrollera om programmet räknar rätt.


# Initial information to the user, 1b
print("\nThis is 1b, where you will be asked to enter a different integer")
input("Press Enter to continue!")

second_int = userint_input("Please type a different integer, then press enter: ")


# Check if different integers where actually used
# If the same were used, only inform, then continue
if second_int == first_int:
    print("\nSadly the second integer: " + str(second_int) +\
          ", was the same as the first integer: " + str(first_int) +\
          "\n")
else:
    print("\nYay, the integers are different, second was: " + str(second_int) +\
          ", and the first was: " + str(first_int) +\
          "\n")

sum1a1b = second_int + first_int

print("The sum of your two integers is:", sum1a1b)

# End this part
input("\nPress Enter to finish!")
print("This is the end of 1b, thank you for playing!")
