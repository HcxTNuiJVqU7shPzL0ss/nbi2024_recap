# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - sports_results_3.py
#
# Veckouppgift 2
# Vecka 3, 13/1
# 3 Sportresultat
#####################################################################


# Starting argument default setting
tie = False


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


print("\nYou will be asked to input the goals of both Tottenham "
      "and Liverpool in the Champions League game.")
print("Please make sure to use integers.")
print("Next you will be asked to select between the four "
      "versions of the program, i.e. which to run.")
input("\nPress Enter to continue.\n")


tottenham = userint_input("How many goals did Tottenham score? ")
liverpool = userint_input("How many goals did Liverpool score? ")

input("\nPress Enter to continue.\n")


if tottenham == liverpool:
    tie = True
    winner = "No team"
elif tottenham > liverpool:
    winner = "Tottenham"
    diff_goals = str(tottenham - liverpool)
else:
    winner = "Liverpool"
    diff_goals = str(liverpool - tottenham)

print("\nSelect which version of the program you want to run."
      "\nInput an integer for your selected option.")
print("\nSelect '1' to show which team that won;\n"
      "Select '2' to display if the game ended in a tie;\n"
      "Select '3' to display the number of more goals the winning team had;\n"
      "Select '4' to display all of the above.")

user_selection = userint_input("\nPlease select your option 1 through 4: ")

if user_selection == 1:
    print("\n" + winner + " won!")
elif user_selection == 2:
    if tie:
        print("\nYes, the game ended in a tie.")
    else:
        print("\nNo, the game did not end in a tie.")
elif user_selection == 3:
    print("\n" + winner + " won with " + diff_goals + " goal(s)!")
elif user_selection == 4:
    if tie:
        print("\nThe game ended in a tie.")
    else:
        print("\n" + winner + " won with " + diff_goals + " goal(s)!")
else:
    print("\nSadly that option was not part of the game!")

input("\nPress enter to end the game!")
