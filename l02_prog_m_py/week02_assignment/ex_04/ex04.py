"""Module for week 2, ex04."""


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


#import sys

from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)#, enter_string,
                                            #enter_int)


print('\nWeek 02, Exercise 04.\n')
press_continue()


def c_to_f(celcius):
    """Use to convert Celsius to Fahrenheit."""
    # (F = (C * 9 / 5) + 32)
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit


# Version 1, simple, no guard.
temp_v1 = input('\nEnter degree Celsius: ')
temp_v1 = float(temp_v1)

print('')
press_continue()

print(c_to_f(temp_v1))

print('')
press_exit()
