# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - discuss.py
#
# Veckouppgift 1
# Vecka 2, 8/1
# 2 Diskutera i grupp
#
# Programmering med Python, 20yhp
#####################################################################


# Defines a ticket price and how much
# money is available prior to purchase
ticket_price = 100 # biljettpris
initial_cash = 200 # pengar på fickan

print("\nExercise 2")

# Calculate how much money is left post purchase
left_over_cash = initial_cash - ticket_price

print("\nDet blir " + str(left_over_cash) + " kronor över.")


# Calculate what half of what money is left will be
half_left_over = left_over_cash / 2

print("\nMy interpretation of fixing an error")
print("Hälften är: " + str(half_left_over) + " kr.")


# Calculate as of original statement in exercise
half_answer = initial_cash - ticket_price/ 2

print("\nUsing original math from exercise")
print("Hälften är: " + str(half_answer) + " kr.")
