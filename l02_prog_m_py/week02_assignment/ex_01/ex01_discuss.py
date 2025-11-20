"""Module for Lesson 02, Week 02, Exercise 01, Discuss."""


#####################################################################
# Copyright 2025 gnoff
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#####################################################################


from my_funct_dir.my_base_functions import (press_continue,
                                            press_goback,
                                            press_exit)


print('\nWeek 02, Exercise 01, Discuss.\n')
press_continue()

# Code example:
# is_member = False
# level1 = 100
# level2 = 300
# discount = 0
#
# price = input("Välkommen, köp något dyrt: ")
# price = float(price)
# if price > level1:
#     print("Grattis! Du har avancerat till nivå 1 och
#     får 10% rabatt.")
#     discount = discount + 10
# if price >= level2:
#     print("Grattis! Du har avancerat till nivå 2 och
#     får 25% rabatt.")
#     discount = discount + 25
#
# final_price = price * (100 - discount) / 100
# print("Efter rabatter blir priset.... " + final_price)


# CONSTANTS shall be ALL_CAPS (pylint, pydocstyle)
# level1 = 100
LEVEL1 = 100
# level2 = 300
LEVEL2 = 300


# Variables
is_member = False
discount = 0

### New code ###
# Ask if user is a member
check_member = ''
while True:
    check_member = input('\nIf you are a member, '
                         'press y, else n: ')
    try:
        if check_member.lower() == 'y':
            is_member = True
            print('\nWelcome member!\n')
            press_continue()
            break
        #elif check_member.lower() == 'n':
        if check_member.lower() == 'n':
            is_member = False
            print('\nSadly, no discount for you!\n')
            press_continue()
            break
        #else:
        print('\nPlease try again!\n')
        press_goback()
        continue
    except ValueError:
        print('\nSomething has gone wrong!\n')
        press_goback()
        continue
### End of new block ###


# price = input("Välkommen, köp något dyrt: ")
# price = float(price)

### New code ###
# Handle check that input can be converted
while True:
    # price = input("Välkommen, köp något dyrt: ")
    price = input("Welcome, buy something: ")
    try:
        price = float(price)
        break
    except ValueError:
        print('\nCannot convert input to float!\n'
              'Try again!')
        press_goback()
        continue
### End of new block ###


# if price > LEVEL1:
#     print("Grattis! Du har avancerat till nivå 1 och får 10% "
#           "rabatt.")
#     discount = discount + 10
# if price >= LEVEL2:
#     print("Grattis! Du har avancerat till nivå 2 och får 25% "
#           "rabatt.")
#     discount = discount + 25
#
# final_price = price * (100 - discount) / 100
# # print("Efter rabatter blir priset.... " + final_price) # BUG
# # Fixed BUG below
# print("Efter rabatter blir priset.... " + str(final_price))

### New code ###
use_discount = False
if is_member:
    if price >= LEVEL2:
        # print("\nGrattis! Du har avancerat till nivå 2 och får 25% "
        #       "rabatt.")
        print("\nCongratulations! You have advanced to Level 2 and will "
              "receive a 25% discount!.")
        discount = discount + 25
        use_discount = True
    elif price >= LEVEL1:
        # print("\nGrattis! Du har avancerat till nivå 1 och får 10% "
        #       "rabatt.")
        print("\nCongratulations! You have advanced to Level 1 and will "
              "receive a 10% discount!.")
        discount = discount + 10
        use_discount = True
    else:
        use_discount = False
else:
    use_discount = False

final_price = price * (100 - discount) / 100

if use_discount:
    # print("\nEfter rabatter blir priset.... " + str(final_price))
    print("\nAfter discount, the price will be: "
          + str(final_price))
else:
    # print("\nUtan rabatter blir priset.... " + str(final_price))
    print("\nWithout discount, the price will be: "
          + str(final_price))
### End of new block ###



# 1. What is the purpose of the code?
print('')
press_continue()
print('\n1. The purpose is to handle discount levels, based on '
      'purchases.')
press_continue()

# 2. Test the code with some different values

# 3. Are there any errors/bugs in the code
# (which cause it to crash).
print('\n3. Yes, there was one bug, now fixed, see comment.')
press_continue()

# 4. Are there any logical errors?
# (The code does something different from what you expect)
print('\n4.1: Does not check if you are member or not.')
print('4.2: Prints both levels if above first time.')
print('4.3: Prints discount, even if you have none.')
print('4.4: Does not handle values which cannot be converted '
      'to float')
print('4.5: Checks level 1 before checking level 2.')
print('4.6: For pylint and pydocstyle, changed CONSTANTS.')
print('4.7: Differs between level 1 and 2, missing a =')

# 5. Discuss possible solutions to bugs.

# 6. Discuss possible improvements.


print('')
press_exit()
