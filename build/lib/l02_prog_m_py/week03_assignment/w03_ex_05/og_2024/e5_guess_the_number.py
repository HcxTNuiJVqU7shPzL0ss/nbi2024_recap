# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - e5_guess_the_number.py
#
# Veckouppgift 3
# Vecka 4, 20/1
# 5 Gissa talet
#####################################################################


"""
Version 1:
Gör ett spel som slumpar ett hemligt tal mellan 1 och 100.
Sedan ska man försöka gissa det. Om man gissar för lågt eller för
högt ska spelet tala om det. Efter att man har gissat rätt ska spelet
skriva ut antalet gissningar.

Version 2:
skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
"Nu börjar det brännas!"
"""


import random

# Generate a "random" number
rand_low = 1
rand_high = 100
rand_no = random.randint(rand_low, rand_high)

guesses = 0 # Starting value for counting guesses
guessed = [] # Empty list to store user guesses
hi_or_lo = None


print('\nWelcome to guess the number game!\nThe AI bot is thinking '
      'about a "random" (integer) number between' , rand_low , 'and',
      rand_high , '\nCan you guess the number?')

input('\nPress Enter to start playing...')


while True:
    try:
        if hi_or_lo is not None:
            print(hi_or_lo)
            print('Guessed so far:' , guessed)

        user_guess = int(input('\nType your (integer) guess, '
                               'finish with enter:\n'))

        if user_guess not in range(rand_low, rand_high + 1, 1):
            print('\nOut of range! (' , rand_low , 'to' ,
                  rand_high , ')')
            continue
        else:
            if user_guess in guessed:
                print('\n\033[91mFYI, you guessed that before!\033[0m\n')

            guesses += 1
            guessed.append(user_guess)
            guessed.sort()

            if user_guess == rand_no:
                print('\nCorrect!' , user_guess , 'was the '
                      'number!' , guesses , 'guesses needed.')
                print('Guesses:' , guessed)
                break
            elif user_guess > rand_no:
                if user_guess in range(rand_no - 5, rand_no + 6, 1):
                    print('You are getting close!')
                print('\nYou guessed too high!')
                input('Press Enter to try again!')
                hi_or_lo = '\nHigh! --> ' + str(user_guess)
                continue
            else:
                if user_guess in range(rand_no - 5, rand_no + 6, 1):
                    print('You are getting close!')
                print('\nYou guessed too low!')
                input('Press Enter to try again!')
                hi_or_lo = '\nLow! --> ' + str(user_guess)
                continue
    except ValueError:
        print('\nNot a valid integer!')
        continue
