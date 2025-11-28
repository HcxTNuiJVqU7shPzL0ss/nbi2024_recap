"""Module for Lesson 02, Week 03, Exercise 03.

Receipt Calculator.
"""

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


import sys


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            press_goback, enter_int)


def w3_ex3_user_input():
    """Use to get user input for the calculator."""
    end_it_clean = ['quit', 'avsluta', 'exit', 'done', 'stop']
    end_it_parens = ['quit()', 'avsluta()', 'exit()', 'done()',
                     'stop()']
    int_list = []
    print('Ex 03 User Input.\nFunction: ',
          w3_ex3_user_input.__name__, sep='')
    print('\nYou will be asked to input integers, representing '
          'what you have purchased.\n'
          'Keep doing this until you want to stop, '
          'then instead type "quit".')
    press_continue()

    print('Welcome to Receipt Buddy (TM)!\n'
          'Exit by enter "quit".\n')

    while True:
        str_in = input('Enter a value:\n')
        clean_string = str_in.replace('\"', '')
        if (clean_string in end_it_clean) or (clean_string in end_it_parens):
            if sum(int_list) == 0:
                print('\nNo values entered, exit hard.')
                sys.exit()
            return sum(int_list)
        try:
            int_in = int(str_in)
            if int_in > 0:
                int_list.append(int_in)
                print('\nValue ' + str(int_in) + ' added.\n')
            else:
                print('\nPlease use a positive integer!')
                press_goback()
            continue
        except ValueError:
            print('\nPlease use an integer!')
            press_goback()
            continue


def w3_ex3_no_ppl():
    """Use to input how many people should split the bill."""
    print('Ex 03 People.\nFunction: ',
          w3_ex3_no_ppl.__name__, sep='')
    print('\nYou will be asked to input an integer.\n'
          'This is to represent how many of you there are that shall '
          'split the bill.')
    press_continue()
    in_string_ppl = 'How many should split the bill: '
    no_of_ppl = enter_int(in_string_ppl)
    print('\n')
    return no_of_ppl


def w3_ex3_tips():
    """Use to enter how much tips to leave.

    If no entry, 10% is standard.
    """
    print('Ex 03 Tips.\nFunction: ',
          w3_ex3_tips.__name__, sep='')
    print('\nYou will be asked to input an integer.\n'
          'This is to represent how tips to leave.\n'
          'If blank, there will be 10% added!')
    press_continue()
    while True:
        s_tip = input('How much tip (in %) to leave: ')
        if len(s_tip) == 0:
            i_tip = 10
            return i_tip
        try:
            i_tip = int(s_tip)
            if i_tip < 0:
                print('\nNegative not allowed!'
                      'Crash!')
                sys.exit()
            if i_tip == 0:
                print('\nReally, 0%?')
            elif i_tip > 20:
                print('\nNow we are generous!')
            return i_tip
        except ValueError:
            print('\nPlease try again!')
            press_goback()
            continue


def w3_ex3_new_calc(the_sum, the_ppl, the_tips):
    """Use to calculate it all."""
    print('Ex 03 Final Calculation.\nFunction: ',
          w3_ex3_new_calc.__name__, sep='')
    print('\nThis is the final calculation.')
    press_continue()
    print('The sum total was: ' + str(the_sum) + ' SEK.')
    print('The number of people was: ' + str(the_ppl) + '.')
    print('The tips to leave was: ' + str(the_tips) + '%.')
    new_sum = the_sum + (the_sum * (the_tips/100))
    per_person = new_sum / the_ppl
    print('Each person shall pay ~' + f'{per_person:.2f}' + ' SEK.')


def main():
    """Use as main function."""
    print('\nWeek 03, Exercise 03, Receipt Calculator.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # Version 1
    res_v1 = w3_ex3_user_input()


    # Version 2
    ppl_v2 = w3_ex3_no_ppl()
    if ppl_v2 < 1:
        print('\nNeed to protect from div by 0!\n'
              '(Also if no of ppl is negative, booo!\n'
              'Hard Exit!')
        sys.exit()
    else:
        shared = res_v1 / ppl_v2


    # Version 3
    the_tip_v3 = w3_ex3_tips()


    # Printouts
    press_continue()
    print('\nVersion 1:\n'
          'The total is: ' + str(res_v1) + ' SEK. Please come back!')
    print('\nVersion 2:\n'
          'You should pay ~' + f'{shared:.2f}' +
          ' SEK per person.')
    print('\nVersion 3:\n'
          'The tip is: ' + str(the_tip_v3) + '%')
    press_continue()

    # Final calculations
    w3_ex3_new_calc(res_v1, ppl_v2, the_tip_v3)


    press_exit()


if __name__ == "__main__":
    main()
