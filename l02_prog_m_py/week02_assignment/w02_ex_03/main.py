"""Module for 'Sports results'.

Lesson 02, Week 02, Exercise 03.
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            enter_int_range)


def ask_goals(team):
    """Use to ask how many goals a team made."""
    low_score_limit = 0 # Cannot score less than 0 goals
    high_score_limit = 149 # Most goals ever scored in a game
    use_score_limit = True
    ask_score = f'Please enter the number of goals {team} scored: '
    scores = enter_int_range(ask_score, low_score_limit,
                             high_score_limit, use_score_limit)
    return scores


def check_game_result():
    """Use to check the results in the game."""
    tottenham_scores = ask_goals('Tottenham')
    liverpool_scores = ask_goals('Liverpool')
    print('')
    if tottenham_scores == liverpool_scores:
        print('The game ended in a tie.')
    elif tottenham_scores > liverpool_scores:
        diff = tottenham_scores - liverpool_scores
        print(f'Tottenham won with {diff} goals.')
    else:
        diff = liverpool_scores - tottenham_scores
        print(f'Liverpool won with {diff} goals.')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Check the results in the game between Tottenham and
    Liverpool in Champions League.
    Ask the user how many goals each team made, then
    print out which team that won.
    """
    print('\nThis is exercise 3, "Sports Results", from week 2.')
    press_continue()

    print('The game is over, time to calculate the result"')
    press_continue()

    check_game_result()

    press_exit()


if __name__ == "__main__":
    main()
