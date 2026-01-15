# pylint: skip-file
# noqa
# Jan Berglund

# Veckouppgift 1
# Vecka 2, 8/1
# 3 Använda variabler och datatyper


# Used to separate each starting point of the assignment
start_line = "\n__________________________________________"


# --------------------------------------------
# 1a Använd input för att be användaren om ett heltal.
# Spara värdet i en variabel.
# Omvandla variabelns värde till ett heltal,
# och skriv ut det för att testa om du har gjort rätt.

# Initial information to the user, 1a
print(start_line)
print("This is 1a, where you will be asked to enter an integer")
input("Press Enter to continue!")

# Ask for and save an integer in a variable
# Throw ValueError if incorrect input, then try again
while True:
    try:
        user_int1a = int(input("Please type an integer, then press enter: "))
        break
    except ValueError:
        print("Not an integer, please try again!")

print("Your selected integer was:", user_int1a)

# End this part
input("Press Enter to finish!")
print("This is the end of 1a, thank you for playing!")


# --------------------------------------------
# 1b Fråga användaren efter ett annat heltal.
# Skriv ut summan av talen, alltså tal1 + tal2.
# Testa genom att hitta på två tal och räkna ut summan i huvudet.
# Kontrollera om programmet räknar rätt.

# Initial information to the user, 1b
print(start_line)
print("\nThis is 1b, where you will be asked to enter a different integer")
input("Press Enter to continue!")

# Ask for and save an integer in a variable
# Throw ValueError if incorrect input, then try again
while True:
    try:
        user_int1b = int(input("Please type a different integer, then press enter: "))
        break
    except ValueError:
        print("Not an integer, please try again!")

# Check if different integers where actually used
# If the same were used, only inform, then continue
if user_int1b == user_int1a:
    print("\nSadly the second integer: " + str(user_int1b) +\
          ", was the same as the first integer: " + str(user_int1a) +\
          "\n")

sum1a1b = user_int1b + user_int1a

print("The sum of your two integers is:", sum1a1b)

# End this part
input("Press Enter to finish!")
print("This is the end of 1b, thank you for playing!")


# --------------------------------------------
# 2a Nu är det dags att köpa vinterkläder.
# Du ser en fin jacka som kostar 2000 kronor.
# Jackan är på rea, 50%.
# Skriv ett program som räknar ut hur mycket du behöver betala.

# Initial information to the user, 2a
print(start_line)
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


# --------------------------------------------
# 2b Gör om programmet så att användaren kan skriva in en procentsats.
# Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med,
# innan du kör det.
# Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.

print(start_line)
print("\nThis is 2b, it will ask you for a discount percentage (as an integer)")
input("Press Enter to continue!")

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

# Check that the input was a valid discount percentage
#if discount_percentage2b < 0 or discount_percentage2b > 100:
#    # Out of range, not OK to continue
#    raise Exception("The selected percentage discount", discount_percentage2b, "is not valid!")

# Calculate the final price
final_price2b = price_initial2a - (price_initial2a * discount_percentage2b / 100)

print("Initial price was " + str(price_initial2a) + " kr, the discount percentage is " +\
      str(discount_percentage2b) + "%")
print("Your price for the jacket will be:", final_price2b, "kr")

# End this part
input("Press Enter to finish!")
print("This is the end of 2b, thank you for playing!")
