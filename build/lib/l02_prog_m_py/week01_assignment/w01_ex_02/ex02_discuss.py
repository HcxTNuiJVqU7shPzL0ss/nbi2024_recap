"""Module for 'Discuss'.

Lesson 02, Week 01, Exercise 02.
Done "off course".
"""

#####################################################################
# Copyright 2025-2026 gnoff
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
                                            press_exit)


def calculate_w1_ex2():
    """Use to calculate week 1, exercise 2.

    This version made for the recap of 2024.
    Subtract ticket price from available funds,
    divide the remainder with two, display what
    the result is.
    """
    ticket_price = 100 # Ticket price
    funds = 200 # Available funds

    # Calculate how much you will have left
    money_left = funds - ticket_price

    # Calculate half of what is left
    half_left = money_left / 2


    print(f'There is {money_left:.2f} SEK left over.')
    print(f'Half of what is left over is: {half_left:.2f} SEK.')

    press_exit()


def main():
    """Use as module for Main.

    This version made for the recap of 2024.
    """
    print('\nLesson 02, Week 01, Exercise 02.')
    press_continue()

    calculate_w1_ex2()


if __name__ == "__main__":
    main()
