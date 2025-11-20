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
                                            press_exit, press_goback,
                                            enter_float)


print('\nWeek 02, Exercise 04.\n')
press_continue()


def c_to_f(celsius):
    """Use to convert Celsius to Fahrenheit, version 1."""
    # (F = (C * 9 / 5) + 32)
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def f_to_c(fahrenheit):
    """Use to convert Fahrenheit to Celsius."""
    # C = 5/9(F-32)
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


def user_float_in(use_temp_internal):
    """Use to enter a (float) value to convert."""
    c = 'Celsius'
    f = 'Fahrenheit'
    if use_temp_internal == 'c':
        conv_from = c
        conv_to = f
    else:
        conv_from = f
        conv_to = c
    in_str_value = 'Please enter a numeric value to ' +\
                    'use for conversion from ' + conv_from +\
                    ' into ' + conv_to + ' : '
    unknown_temp = enter_float(in_str_value)
    return unknown_temp


def ask_c_or_f():
    """Use to ask of to input C or F value, version 2."""
    while True:
        use_temperature = input('\nDo you want to assign '
                                'temperature in (c) celsius '
                                'or (f) fahrenheit: ')
        celsius = ('c', '(c)', '(c) celsius', 'celsius')
        fahrenheit = ('f', '(f)', '(f) fahrenheit', 'fahrenheit')
        try:
            if use_temperature in celsius:
                ret_temp = 'c'
                return ret_temp
            if use_temperature in fahrenheit:
                ret_temp = 'f'
                return ret_temp
            print('\nTry again.\n')
            press_goback()
            continue
        except ValueError:
            print('\nPlease try again.\n')
            press_goback()
            continue


def do_conversion():
    """Perform the act of conversion."""
    c = 'Celsius'
    f = 'Fahrenheit'
    output_string = 'The converted temperature is: '
    use_temp = ask_c_or_f()
    temperature = user_float_in(use_temp)
    if use_temp == 'c':
        result_f = c_to_f(temperature)
        print('\n' + output_string + str(result_f) + ' ' + f)
        c_temp = temperature
    else:
        result_f = f_to_c(temperature)
        print('\n' + output_string + str(result_f) + ' ' + c)
        c_temp = result_f
    return c_temp


def check_temperature(celsius_now):
    """Use to check if to print a message, version3."""
    if celsius_now < 10.0:
        print('\nPlease put on winter clothes, it is '
              'cold out there today!\n')
    elif celsius_now >= 20.0:
        print('\nSuggest to bring a swimsuit, it is '
              'hot out there today!\n')


# Perform most actions, and get actual degrees in Celsius.
actual_c = do_conversion()

# Check if to print a message based or current temperature.
check_temperature(actual_c)


print('')
press_exit()
