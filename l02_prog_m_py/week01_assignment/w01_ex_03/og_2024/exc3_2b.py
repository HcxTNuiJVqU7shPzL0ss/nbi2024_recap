# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - exc3_2b.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper
# 2b
#####################################################################


# 2b Gör om programmet så att användaren kan skriva in en procentsats.
# Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med,
# innan du kör det.
# Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

print("\nThis is 2b, it will ask you for a discount percentage (as an integer)")
input("Press Enter to continue!")

# Base values to use, as of assignment
price_initial = 2000


# Ask for and save an integer in a variable
# Throw ValueError if incorrect input, then try again
while True:
    try:
        discount_percentage2b = int(input("Please type the discount as an integer,"
            " range 0 to 100, then press enter: "))
        # Check that the input was a valid discount percentage
        if discount_percentage2b < 0 or discount_percentage2b > 100:
            print("The selected percentage discount", discount_percentage2b, "is not valid!")
            continue
        else:
            break
    except ValueError:
        print("Not an integer, please try again!")


# Calculate the final price
final_price2b = price_initial - (price_initial * discount_percentage2b / 100)

print("Initial price was " + str(price_initial) + " kr, the discount percentage is " +\
      str(discount_percentage2b) + "%")
print("Your price for the jacket will be:", final_price2b, "kr")

# End this part
input("Press Enter to finish!")
print("This is the end of 2b, thank you for playing!")
