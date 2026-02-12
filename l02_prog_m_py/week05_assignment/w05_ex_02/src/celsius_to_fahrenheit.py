"""Module for Lesson 02, Week 05, Exercise 02, part 1.

Part 2.1 function.
See file w05_ex02_functions for "just following the exercise"
version of "easier not as complete" version.
This one here can be considered extensive and very
overworked, used for learning things.
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
                                            enter_float)


def celsius_to_fahrenheit(c_degree_input):
    """Use to convert degree Celsius to Fahrenheit.

    Will raise TypeError if input is anything but an int or a
    float.
    Will raise ValueError if input is less than the absolute zero,
    or greater than the Planck temperature.
    """
    # Store the function first parameter name from
    # celsius_to_fahrenheit
    param_name_c_degree = dir()[0]
    # Do NOT add any variable above the line that contains "dir"

    absolute_zero = -273.15
    too_hot = 1.416785e32 # Planck temperature (approx), K

    if (isinstance(c_degree_input, bool) or
            not isinstance(c_degree_input, (int, float))):
        wrong_type = type(c_degree_input)
        raise TypeError(f'\nNeed a number for parameter: '
                        f'{param_name_c_degree}.\n'
                        f'What was entered is of type: '
                        f'{wrong_type}')

    if c_degree_input < absolute_zero or c_degree_input > too_hot:
        raise ValueError(f'\nThe input temperature must be at least: '
                        f'{absolute_zero} (or above).\n'
                        f'Though it also needs to be maximum at '
                        f'{too_hot} (or below).\n'
                         f'Your input was: {c_degree_input}.')

    # Perform temperature conversion calculation
    return c_degree_input * 9 / 5 + 32


def run_c_to_f_conversion():
    """Use to ask for a temperature to convert.

    User should input a float in Celsius, this will be converted
    into Fahrenheit, then presented.
    """
    print('You will be asked to input a float value.\n'
          'This represents a temperature in Celsius.\n'
          'The input value will be converted into Fahrenheit, '
          'then presented as a result.')
    press_continue()
    ask_str = 'Please enter a value for degrees Celsius: '
    use_to_convert = enter_float(ask_str)
    is_fahrenheit = celsius_to_fahrenheit(use_to_convert)
    print(f'\nYour value "{use_to_convert}" in Celsius '
          f'is {is_fahrenheit} degrees Fahrenheit.')
