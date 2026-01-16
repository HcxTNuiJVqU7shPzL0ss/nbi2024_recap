"""Module for 'More exercises'.

Lesson 02, Week 01, Exercise 04, Parts: 1a, 1b, 1c, 2, 3a and 3b.
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


from datetime import date, timedelta


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            enter_int_range)


def time_set(seconds):
    """Use to convert seconds.

    From seconds into whole hours and minutes.
    """
    hours = seconds // 3600 # How many hours
    seconds %= 3600 # Remaining seconds
    minutes = seconds // 60 # How many minutes
    seconds %= 60 # Remaining seconds

    return f'{hours:.0f} h, {minutes:.0f} min, {seconds:.0f} sec'


def ex4_1_sthlm_gbg_trip():
    """Use as module for parts 1a, 1b and 1c of Exercise 4.

    Calculate time to drive between Stockholm (sthlm) and
    Gothenburg (gbg).
    Display the time in various ways.
    """
    dist_sthlm_gbg_km = 470
    speed_low_limit = 80
    speed_high_limit = 110
    use_range = True

    # Intro
    print('\nThis is part 1 of exercise 4.\n'
          'Display the time to drive between Stockholm and '
          'Gothenburg.\n'
          'You will be asked to input your desired average '
          'speed to drive in km/h.')
    press_continue()

    # 1a
    print('This is part 1a, time in hours.')
    speed_string = 'How fast, in km/h, do you want to drive: '

    # Velocity in km/h, set range min 80, max 110 km/h
    speed_kmh = enter_int_range(speed_string, speed_low_limit,
                                speed_high_limit, use_range)

    # Velocity in m/s
    speed_mps = (speed_kmh * 1000) / 3600
    # Time in seconds
    no_of_sec = (dist_sthlm_gbg_km * 1000) / speed_mps
    no_of_hours = no_of_sec / 3600
    print(f'\n(1a) It will take ~{no_of_hours:.2f} h to drive '
          f'at that speed.')
    press_continue()

    # 1b
    print('\nThis is part 1b, time in minutes.')
    no_of_min = no_of_sec / 60
    print(f'\n(1b) It will take ~{no_of_min:.2f} min to drive '
          f'at that speed.')
    press_continue()

    # 1c
    print('\nThis is part 1c, time in whole hours, whole minutes, '
          'and remaining seconds.')
    display_time = time_set(no_of_sec)
    print(f'\n(1c) The time to drive at {speed_kmh} km/h '
          f'is {display_time}.')
    press_continue()


def ex4_2_calc_hypotenuse():
    """Use as module for part 2 of Exercise 4.

    Calculate the hypotenuse in a right triangle, given the two
    shorter sides by user input.
    """
    side1_str = 'Enter the length of side 1 of the triangle: '
    side2_str = 'Enter the length of side 2 of the triangle: '
    # Require low limit for any side to be 1 (int)
    side_low_limit = 1
    # Require high limit for any side to be 99 (int)
    side_high_limit = 99
    use_range = True
    # 2
    print('This is part 2, enter the two sides of a right '
          'triangle, you will get the hypotenuse length calculated.')
    press_continue()
    # Get user input
    side1_length = enter_int_range(side1_str, side_low_limit,
                                   side_high_limit, use_range)
    side2_length = enter_int_range(side2_str, side_low_limit,
                                   side_high_limit, use_range)
    # Calculate the hypotenuse squared
    hypo_squared = (side1_length ** 2) + (side2_length ** 2)
    # Get the hypotenuse
    hypotenuse = hypo_squared ** 0.5
    print(f"\nThe hypotenuse given side 1 as {side1_length} "
          f"and side 2 as {side2_length} is: {hypotenuse:.2f}.")
    press_continue()


def ex4_3_display_date():
    """Use as module for parts 3a and 3b of Exercise 4.

    3a: Display today's date.
    3b: Display what the date will be in 7 days.
    """
    # 3a
    print('\nThis is part 3a, today\'s date.')
    date_today = date.today()
    print(f'\nThe date today is: {date_today}')
    press_continue()

    # 3b
    print('This is part 3b, the date in 7 days.')
    date_in_seven = date_today + timedelta(days=7)
    print(f'\nThe date in 7 days is: {date_in_seven}')


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    """
    ex4_1_sthlm_gbg_trip()
    ex4_2_calc_hypotenuse()
    ex4_3_display_date()
    press_exit()


if __name__ == "__main__":
    main()
