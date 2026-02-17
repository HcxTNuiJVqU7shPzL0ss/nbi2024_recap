"""Module for Lesson 02, Exam.

Use to handle print to user commands.
"""

#####################################################################
# Copyright 2026 gnoff
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


from my_funct_dir.my_base_functions import press_continue, y_or_n


def print_commands(command_check, inventory_list):
    """Use to check and handle commands for print status.

    A valid command was entered, as of:
    i: Print user inventory
    h: Help == Print help info
    # Exam Version 1: F ('i' prints user inventory).
    """
    help_info = ('\n--------------------------------------\n\n'
                 'Your available commands are\n\n'
                 'W: Move up\n'
                 'S: Move down\n'
                 'A: Move left\n'
                 'D: Move right\n\n'
                 'I: Print inventory\n'
                 'H: Display commands\n\n'
                 'Q: Quit (quit game)\n'
                 'X: Exit (exit game)\n'
                 '\n--------------------------------------')
    if command_check == 'i':  # print inventory
        if not inventory_list:
            print('\nThe inventory is empty.')
        else:
            print('\nInventory')
            for i, item in enumerate(inventory_list):
                print(f'{i + 1}: {item}')

    elif command_check == 'h': # print help
        print(help_info)
    press_continue()


def print_welcome_info():
    """Use to print initial welcome information.

    Also asks user if negative values are to be used, or not.
    """
    # Ask if to allow negative values
    ask_negative = ('Do you wish to allow negative values, '
                    '(y)es or (n)o: ')

    # Print welcome message and info
    print('\nWelcome to an exciting game: Fruit Loop!')
    print_commands('h', [])

    print('You are the player on the board, starting in the '
          'middle, look for your marker: @\n\n'
          'Around the edges are impassable walls, signified '
          'by the following: ■\n\n'
          'There are a few internal walls, which cannot be '
          'passed, unless you have found a pickaxe. These '
          'internal walls looks like this: #\n\n'
          'The goal of this exciting game is to pick up things '
          'from the board, items can be found where you see: ?')
    press_continue()
    print('For help with commands, please select "h" '
          'as your command.')
    press_continue()
    print('Due to "The Floor is Lava", you will lose one (1) point '
          'for each movement when you do not find anything.\n'
          'Also, traps will have you lose 10 points.\n'
          'Either 0 can be the lowest score, or you can have '
          'negative score.')
    press_continue()

    check_neg = y_or_n(ask_negative)

    if check_neg == 'y':
        print('\nOK, negative values are possible!')
        return True
    print('\nOK, 0 will be the lowest value for score.')
    return False
