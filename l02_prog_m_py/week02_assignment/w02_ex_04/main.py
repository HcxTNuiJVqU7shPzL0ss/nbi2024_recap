"""Module for 'Temperature conversion'.

Lesson 02, Week 02, Exercise 04.
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
                                            enter_float,
                                            press_goback)


def user_message(temperature):
    """Use to check if to display a message to the user.

    If below 10C, bring warm clothes.
    If at least 20C, suggest a bathing suit.
    """
    if temperature < 10:
        message = 'It is cold out there, please wear warm clothes.'
    elif temperature >= 20:
        message = 'It is warm, suggest to bring a swim suit.'
    else:
        message = None
    return message


def convert_temperature(selected_scale):
    """Use to convert temperature.

    Parameter selected_scale sets which scale is selected as base.
    If Fahrenheit is selected, convert to Celsius.
    If Celsius is selected, convert to Fahrenheit.
    Return the converted value.
    """
    enter_temp = (f'Please enter your temperature '
                  f'in {selected_scale}: ')
    print('')
    input_temp = enter_float(enter_temp)
    if 'C' in selected_scale:
        conv_temp = (1.8 * input_temp) + 32
        any_message = user_message(input_temp)
    else:
        conv_temp = (input_temp - 32) / 1.8
        any_message = user_message(conv_temp)
    return [input_temp, conv_temp, any_message]


def select_scale():
    """Use to select from which scale to enter a temperature."""
    celsius = ('c', '(c)', '(c)elsius', 'celsius')
    fahrenheit = ('f', '(f)', '(f)ahrenheit', 'fahrenheit')
    while True:
        scale = input('Do you want to use (F)ahrenheit or '
                      '(C)elsius as your scale: ')
        try:
            if scale.casefold() in celsius:
                temp_scale = 'Celsius'
                return temp_scale
            if scale.casefold() in fahrenheit:
                temp_scale = 'Fahrenheit'
                return temp_scale
            print('\nIncorrect option, please try again.')
            press_goback()
            continue
        except ValueError:
            press_goback()
            continue


def enter_and_display_temperature():
    """Use to enter a temperature.

    Also display the converted result.
    """
    base_scale = select_scale()
    if 'C' in base_scale:
        into_temp = 'Fahrenheit'
    else:
        into_temp = 'Celsius'
    converted_value = convert_temperature(base_scale)
    press_continue()
    print(f'You entered {converted_value[0]:.2f} in {base_scale}.')
    print(f'The converted value is {converted_value[1]:.2f} '
          f'in {into_temp}')
    if converted_value[2] is not None:
        print(converted_value[2])


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Convert temperature between Celsius and Fahrenheit.
    """
    print('\nThis is exercise 4, "Temperature Conversion", '
          'from week 2.')
    press_continue()

    enter_and_display_temperature()

    press_exit()


if __name__ == "__main__":
    main()
