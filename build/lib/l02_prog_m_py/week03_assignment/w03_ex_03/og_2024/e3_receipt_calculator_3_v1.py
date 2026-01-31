# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e3_receipt_calculator_3_v1.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 3 Kvittouträknaren / version 1 (v1)
#####################################################################


import sys


"""
Gör ett program som upprepade gånger ber användaren skriva in ett tal.
När man skriver in strängen "quit" eller "avsluta" ska programmet ska
det räkna ut summan av talen. Exempel:
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 25
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Det blir 75 kr totalt. Välkommen åter!
Tips! För att lösa uppgiften behöver du: flera variabler, input, while-loop.
"""

print('\n...................."3.v1"....................')
print('\nYou will be asked to input numbers, as int or float. '
      '\nTo exit type "q" or "quit".')
input("\nPress enter to continue")

sum_tot = 0.0

while True:
    user_inp = input('\nType a value, or "quit" to exit'
                       ', then press enter.\n')
    user_inp = user_inp.lower()
    if user_inp in ("q", "quit", "avsluta"):
        break
    else:
        try:
            num_i = int(user_inp) # Check if int
            num_numeral = abs(num_i) # Make sure number is positive
            sum_tot += num_numeral
            continue
        except ValueError:
            try:
                num_f = float(user_inp) # Check if float
                num_numeral = abs(num_f) # Make sure number r is positive
                sum_tot += num_numeral
                continue
            except ValueError: # Input not option to quit, nor int or float
                print("Selected input not integer or float!")
                print("Please try again...")
                continue

sum_tot = float(sum_tot)

if sum_tot != 0.0:
    print('\nThe total is:', sum_tot, 'SEK')
else:
    print('Sum is 0, nothing to see here!')
    sys.exit('\nBoom!\n')
