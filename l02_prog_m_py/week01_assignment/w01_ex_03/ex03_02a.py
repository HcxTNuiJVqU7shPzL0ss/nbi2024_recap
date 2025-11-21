"""Module for Lesson 02, Week 01, Exercise 03, Part 02a."""

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
                                            press_exit)


def main():
    """Use as main in ex 03 part 02a."""
    print('\nExercise 3, part 2a.')
    press_continue()

    orig_price = 2000
    discount = 50

    disc_price = orig_price - (orig_price * (discount / 100))

    print('\nThe original price was:', orig_price, 'SEK.')
    print('The discount was:', str(discount) + '%')
    print('Your discounted price is: ', f'{disc_price:.2f}',
          ' SEK.', sep = '')
    press_exit()


if __name__ == "__main__":
    main()
