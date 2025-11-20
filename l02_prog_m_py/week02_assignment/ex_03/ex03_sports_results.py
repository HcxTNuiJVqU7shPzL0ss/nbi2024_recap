"""Module for Lesson 02, Week 02, Exercise 03, Sports results."""


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
                                            press_exit, enter_string,
                                            enter_int)


print('\nWeek 02, Exercise 03, Sports results.\n')
press_continue()


def soccer():
    """Use to enter input for the soccer game."""
    # CONSTANT PEP8
    max_goals = 149

    # Variables
    #team_1 = ''
    s_in_team_1 = ('What is the name of the home team '
                   '(e.g., Tottenham): ')
    #team_2 = ''
    s_in_team_2 = ('What is the name of the away team '
                   '(e.g., Liverpool): ')

    # User shall enter the name of the home team
    team_1 = enter_string(s_in_team_1)
    # User shall enter the name of the away team
    team_2 = enter_string(s_in_team_2)

    # Not allowed identical names.
    if team_1.lower() == team_2.lower():
        print('\nYou entered the same name for both teams!\n'
              'Will not continue, run again.')
        sys.exit()


    # Variables
    #goals_1 = 0
    s_in_goals_1 = 'How many goals did ' + team_1 + ' score: '
    #goals_2 = 0
    s_in_goals_2 = 'How many goals did ' + team_2 + ' score: '

    # User shall enter the number of goals scored of the home team
    goals_1 = enter_int(s_in_goals_1, 0, 0, False)
    # User shall enter the number of goals scored of the away team
    goals_2 = enter_int(s_in_goals_2, 0, 0, False)

    # Not allowed negative number of goals.
    if (goals_1 < 0) or (goals_2 < 0):
        print('\nNegative number of goals not allowed!\n'
              'Will not continue, run again.')
        sys.exit()


    if goals_1 > goals_2:
        diff = goals_1 - goals_2
        print('\n' + team_1, 'won!\n'
              'They scored', diff, 'more goals.')
    elif goals_2 > goals_1:
        diff = goals_2 - goals_1
        print('\n' + team_2, 'won!\n'
              'They scored', diff, 'more goals.')
    elif goals_1 == goals_2:
        print('\nIt was a tie!\n') # Version 2


    tot_goals = goals_1 + goals_2
    if tot_goals > 149:
        print('\nRecord broken! Previous:', max_goals)


# Call the function
soccer()


print('')
press_exit()
