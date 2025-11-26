"""Module for Lesson 02, Week 01, Exercise 04, Part 01a."""

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
                                            press_exit,
                                            enter_int_range)


def stockholm_gbg_main():
    """Use as main function for Stockholm to Göteborg."""
    distance = 470 # Nr of km between Stockholm and Göteborg
    in_string = 'How fast, in km/h, do you want to drive: '

    # Velocity in km/h
    speed_kmh = enter_int_range(in_string, 50, 120, True)

    # Velocity in m/s
    speed_mps = (speed_kmh * 1000) / 3600

    no_of_sec = (distance * 1000) / speed_mps
    return no_of_sec


def main():
    """Use as Main for part 01a."""
    print('\nExercise 4, part 1a.')
    press_continue()

    nr_of_sec = stockholm_gbg_main()

    press_continue()

    print('\nIt will take you', f'{nr_of_sec:.2f}',
          'seconds to drive.')
    press_exit()


if __name__ == '__main__':
    main()
