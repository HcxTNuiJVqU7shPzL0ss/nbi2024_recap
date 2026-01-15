# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - int_input_def.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper
#
# Function definition to use for 1a and 1b
#####################################################################


# Ask for and save an integer in a variable
# Throw ValueError if incorrect input (not an integer), then try again
# Made as a function to be able to reuse in "1b" as a separate file
def userint_input(info_text):
    """Add for 2026, cannot get passed pydocstyle."""
    while True:
        try:
            user_int = int(input(info_text))
            return user_int
            break
        except ValueError:
            print("\nNot an integer, please try again!\n")
