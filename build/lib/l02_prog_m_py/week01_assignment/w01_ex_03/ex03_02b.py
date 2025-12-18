"""Module for Lesson 02, Week 01, Exercise 03, Part 02b."""

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


def main():
    """Use as main module for ex 03, part 02b."""
    print('\nExercise 3, part 2b.')
    press_continue()

    orig_price = 2000
    input_string = 'Enter a discount as integer (in %): '


    discount = enter_int_range(input_string, 0, 100, True)

    disc_price = orig_price - (orig_price * (discount / 100))

    print('\nThe original price was:', orig_price, 'SEK.')
    print('The discount was:', str(discount) + '%')
    print('Your discounted price is:', f'{disc_price:.2f}', 'SEK.')

    if discount == 0:
        print('\nNo discount!')
    elif discount > 100: # Should not be possible
        print('\nWell, that is not how it works! '
              'Typically you do not make money by '
              'buying stuff!')
    elif discount == 100:
        print('\nWow! Free stuff!')

    press_exit()


if __name__ == '__main__':
    main()
