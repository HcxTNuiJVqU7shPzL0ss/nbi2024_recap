# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - exc3_2a.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper
# 2a
#####################################################################


# 2a Nu är det dags att köpa vinterkläder.
# Du ser en fin jacka som kostar 2000 kronor.
# Jackan är på rea, 50%.
# Skriv ett program som räknar ut hur mycket du behöver betala.

# Initial information to the user, 2a
print("\nThis is 2a, it will let you know the final cost of your jacket")
input("Press Enter to continue!")

# Base values to use, as of assignment
price_initial2a = 2000
discount_percentage2a = 50

# Calculate the final price
final_price2a = price_initial2a * discount_percentage2a / 100

print("Initial price was " + str(price_initial2a) + " kr, the discount percentage is " +\
      str(discount_percentage2a) + "%")
print("Your price for the jacket will be:", final_price2a, "kr")

# End this part
input("Press Enter to finish!")
print("This is the end of 2a, thank you for playing!")
