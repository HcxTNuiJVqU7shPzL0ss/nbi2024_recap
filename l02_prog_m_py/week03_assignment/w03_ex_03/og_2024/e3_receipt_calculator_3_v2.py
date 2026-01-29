# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e3_receipt_calculator_3_v2.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 3 Kvittouträknaren / version 2 (v2)
#####################################################################


"""
Version 2: programmet ska fråga hur många man är,
och tala om hur mycket varje person i sällskapet ska betala.
Hur många är ni? 3
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!
"""


# Run version 1 and import the variable
import e3_receipt_calculator_3_v1


input("\nPress enter to continue")

print('\n...................."3.v2"....................')
print('\nYou will be asked how many persons you are, '
      'only one integer input is accepted.')


# Ask for input by the user
# Check if an integer has been entered, if OK continue with value
# If integer was not entered, ask to retry until it works
# Treat a negative value as positive, a negative value is not
# feasible.
while True:
    try:
        no_ppl = int(input('\nPlease input number of people in, '
                           'your party, only use integer: '))
        no_ppl = abs(no_ppl)
        if no_ppl == 0: # Ensure you do not end up with "division by zero"
            print('\nZero is not allowed!')
            continue
        else:
            break
    except ValueError:
        print("\nSelected input not an integer, please retry.\n")
        continue

price_per_person = e3_receipt_calculator_3_v1.sum_tot / no_ppl

# Round to max 2 decimals
price_per_person = round(price_per_person,2)

print('\nPrice in total is:', e3_receipt_calculator_3_v1.sum_tot, 'SEK')
print('Number of persons in your party is:', no_ppl)
print('Divided equally, you should each pay:', price_per_person, 'SEK')
