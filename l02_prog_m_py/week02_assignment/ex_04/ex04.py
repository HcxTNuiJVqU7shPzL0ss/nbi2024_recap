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
                                            press_exit, enter_float)#, enter_string,
                                            #enter_int)


print('\nWeek 02, Exercise 04.\n')
press_continue()


def c_to_f(celcius):
    """Use to convert Celsius to Fahrenheit."""
    # (F = (C * 9 / 5) + 32)
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit


def f_to_c(fahrenheit):
    """Use to convert Fahrenheit to Celsius."""
    # C = 5/9(F-32)
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


def user_interaction():
    in_str_value = 'Please enter a numeric value: '
    unknown_temp = enter_float(in_str_value)
    return unknown_temp

# Version 2, temp, simple, not done.
temp_v2 = user_interaction()


print('')
press_continue()

print(f_to_c(temp_v2))

print('')
press_exit()
