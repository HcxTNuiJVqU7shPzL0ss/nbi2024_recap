# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - discuss_1.py
#
# Veckouppgift 2
# Vecka 3, 13/1
# 1 Diskutera i grupp
#####################################################################


# Initial default variable declarations
is_member = False   # Used to determine if member or not
level1 = 100        # First level for discount
level2 = 300        # Second level for discount
discount = 0        # Discount, in percentage


# Ask for and save a number in a variable, for "price"
# Throw ValueError if incorrect input (not int or float), then try again
# Negative numbers seen as positive
print("\nYou will be asked to input the price as int or float")
input("Press Enter to continue!\n")
while True:
    price = input("Welcome, please enter the price: ")
    try:
        price_i = int(price)                # Check if int
        price_numeral = abs(price_i)        # Make sure positive
        break
    except ValueError:
        try:
            price_f = float(price)          # Check if float
            price_numeral = abs(price_f)    # Make sure positive
            break
        except ValueError:                  # Input not int or float
            print("Selected input not integer or float!")
            print("Please try again...")
            continue


# Ask for and save an integer in a variable, to check if member
# Throw ValueError if incorrect input, then try again
# Negative numbers seen as positive
print("\nYou will be asked if you are a member, please answer by input of int")
input("Press Enter to continue!\n")
while True:
    try:
        member_check = int(input("If you are a member, please type 1, "
                                 "else any other integer (then hit enter): "))
        member_check = abs(member_check)
        break
    except ValueError:
        print("Not an integer, please try again!")


if member_check == 1:   # 1 == member, set as True, else keep as False
    is_member = True

price_numeral = float(price_numeral)    # Ensure float is used

# Check if member, then check if price warrants a discount
if is_member:
    if price_numeral >= level2:
        print("\nCongratulations! You have advanced to Level 2, "
              "and will receive 25% discount.")
        discount = discount + 25
    elif price_numeral > level1:
        print("\nCongratulations! You have advanced to Level 1, "
              "and will receive 10% discount.")
        discount = discount + 10
    else:
        print("\nSorry, the price does not warrant a discount.")
else:
    print("\nYou are not a member, hence you will not receive"
          "any discount.")
input("Press Enter to continue!\n")

final_price = price_numeral * (100 - discount) / 100

print("\nYour price, including any discount, "
      "is: " + str(final_price))
input("Press Enter to continue!\n")
