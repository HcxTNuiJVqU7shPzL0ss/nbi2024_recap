# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - temp_convert_4.py
#
# Veckouppgift 2
# Vecka 3, 13/1
# 4 Temperaturomvandling
#####################################################################


# Ask for and save an integer (or float) in a variable
# Throw ValueError if incorrect input (not an integer/float),
# then try again
# Accept and keep negative numbers as is
def userint_input(info_text):
    # noqa
    while True:
        user_in = input(info_text)
        try:
            user_int = int(user_in)
            user_int = float(user_int)
            return user_int
        except ValueError:
            try:
                user_float = float(user_in)
                return user_float
            except:
                print("\nNot an integer or float!\n"
                      "Please try again!\n")


print("\nYou will be asked to select which scale to enter your "
      "temperature in, Celsius or Fahrenheit.")
input("\nPress enter to continue")

# Wait for appropriate response from the user
while True:
    user_scale = input("\nSelect 'C' for Celsius, or 'F' for "
                       "Fahrenheit, then press enter.\n")
    user_scale = user_scale.upper()
    if user_scale in ("C", "F"):
        break
    else:
        print("\nUnknown option, please try again!")
        continue

print("\nYou selected " + user_scale)

print("\nYou will be asked to select enter your temperature "
      "in " + user_scale + ".")
input("\nPress enter to continue")

user_temp = userint_input("\nSet your temperature: ")

print("\nYour entered temperature is" , user_temp , user_scale)
input("\nPress enter to continue")


# Temperature conversions
if user_scale == "C":
    temp_f = ((1.8 * user_temp) + 32)
    temp_c = user_temp
else:
    temp_f = user_temp
    temp_c = ((user_temp - 32) / 1.8)

temp_f = round(temp_f, 2)
temp_c = round(temp_c, 2)

print("\nTemp in C is " + str(temp_c))
print("Temp in F is " + str(temp_f))

input("\nPress enter to continue")


# Check to see if advising regarding clothes or not
advice = (temp_c < 10 or temp_c >= 20)

if not advice:
    print("\nNothing more to see here, please move along!")
elif temp_c < 10:
    print("\nPlease make sure to wear enough clothes in the cold!")
else:
    print("\nSuggest that you ensure to pack clothes for going swimming!")
