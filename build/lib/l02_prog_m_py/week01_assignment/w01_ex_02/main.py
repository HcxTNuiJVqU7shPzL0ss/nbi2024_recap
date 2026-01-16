"""Module for 'Discuss'.

Lesson 02, Week 01, Exercise 02.
TAP HT 25D.
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


def calculate_money_left():
    """Use to calculate week 1, exercise 2.

    This version made for 2025 (and 2026), TAP HT 25D.
    Start money (funds), subtract ticket price, then divide
    money left over to share equally with a friend.
    """
    ticket_price = 100 # Ticket price
    funds = 200 # Available funds

    # Calculate how much you will have left
    money_left = funds - ticket_price

    # Calculate half of what is left, to share
    half_left = money_left / 2


    print(f'\nThere is {money_left:.2f} SEK left after '
          f'purchase of the ticket.')
    print(f'Each person will get {half_left:.2f} SEK.')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    calculate_money_left()


if __name__ == "__main__":
    main()
