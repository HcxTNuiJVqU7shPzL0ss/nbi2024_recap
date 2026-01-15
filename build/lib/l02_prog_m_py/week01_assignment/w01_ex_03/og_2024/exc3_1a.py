# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - exc3_1a.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper
# 1a
#####################################################################


# Import function, mainly to be able to rerun "1a"
# This is to be able to have 1a and 1b in separate files
from int_input_def import userint_input


# 1a Använd input för att be användaren om ett heltal.
# Spara värdet i en variabel.
# Omvandla variabelns värde till ett heltal,
# och skriv ut det för att testa om du har gjort rätt.

# Initial information to the user, 1a
print("\nThis is 1a, where you will be asked to enter an integer")
input("Press Enter to continue!\n")

user_int = userint_input("Please type an integer, then press enter: ")

print("\nYour selected integer was:", user_int)

# End this exercise
input("\nPress Enter to finish!")
print("This is the end of 1a, thank you for playing!")
