# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - balder_2.py
#
# Veckouppgift 2
# Vecka 3, 13/1
# 2 Balder
#####################################################################


# Initial declaration(s)
min_length = 130 # Minimum length to be allowed to ride Balder (in cm)


# Information to the user
print("\nYou will be asked for your length in centimeters, "
      "the reason is to check if you will be allowed to "
      "ride Balder at Liseberg.")
input("Press Enter to continue\n")


# Ask for input by the user
# Check if an integer has been entered, if OK continue with value
# If integer was not entered, ask to retry until it works
# Treat a negative value as positive, a negative value is not
# feasible.
while True:
    try:
        user_length = int(input("\nPlease input your length in cm, only "
                            "use integer: "))
        user_length = abs(user_length)
        break
    except ValueError:
        print("\nSelected input not an integer, please retry.\n")
        continue


# Check if allowed to ride Balder
input("\nPress Enter to continue!")
if user_length >= min_length:
    print("\nWhohoo, you are allowed to ride!") # "Du får åka!"
else:
    print("\nOh no, you have to use the kids rides instead!") # "Du får inte åka"


#################################################################


# Extra silly stuff

import sys

user_newborn = 49 # Less than the average newborn (full-term)
user_toddler = 88 # Googled average of walking age kids
user_little_person = 147 # Max height to be defined as a little person
user_too_tall = 230 # Likely safety hazards with this length and amusement parks
user_not_feasible = 273 # Taller than the known tallest man ever

input("\nPress Enter to continue!")
check_silly = input("\nDo you want to continue with silly stuff?\n"
                    "If press 'y' then enter, else just enter.\n")

# Make sure both lower (y) and upper (Y) case is accepted
check_silly = check_silly.lower()

if check_silly != "y":
    print("\nNo worries, thanks and bye!")
    sys.exit(0)

print("Your stated length was:" , user_length , "cm")

if user_length <= user_newborn:
    print("\nSeriously? Are you old enough to use this?")
    print("Are you sure you input your length in centimeters?")
    print("The average length of a newborn is 49 cm.")
elif user_length <= user_toddler:
    print("\nYou state you are taller than a newborn, but your height "
          "is less than the average height of a toddler at walking age?")
    print("Are you sure you should be considering Balder?")
elif user_length <= user_little_person:
    print("\nAll hail Warwick Davis!")
elif user_length >= user_not_feasible:
    print("\nYou should be calling Guinness mate!"
          "\nAre you really taller than Robert Wadlow was?")
elif user_length >= user_too_tall:
    print("\nWith your height make sure to stay safe at the ride!")
else:
    print("\nYou seem to be of normal adult height, boring!")

input("\nPlease press enter to exit!")

sys.exit("End of all the silly stuff as well")
