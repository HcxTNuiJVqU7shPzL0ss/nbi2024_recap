"""Module for 'Poker Hand'.

Lesson 02, Week 04, Exercise 04.
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


# pylint: disable=import-error
from ex04_extra_calls import run_game
from force_hands import run_forced_hands
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Practice functions and modules.
    """
    print('\nThis is exercise 4, "Poker Hand", '
          'from week 4.')
    press_continue()

    force = False
    forced_list = []

    # Run all functions
    run_game(force, forced_list)

    press_continue()

    # Run a forced test over all hands
    run_forced_hands()

    press_exit()


if __name__ == "__main__":
    main()
