"""Module for Lesson 02, Week 04, Exercise 05.

Turtle graphics.
"""

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


import turtle as t


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def draw_square(side_pixels):
    """Use to draw a square using Turtle graphics."""
    for side in range (4):
        t.forward(side_pixels) # Draw a side with length "side_pixels"
        t.left(90) # Turn 90 degrees


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 05, Turtle graphics.'
          '\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # Exercise 1: Function that draws a square with length of side
    # as parameter.
    draw_square(200)


    # Allow the window to stay until user close it
    t.mainloop()
    press_exit()


if __name__ == "__main__":
    main()
