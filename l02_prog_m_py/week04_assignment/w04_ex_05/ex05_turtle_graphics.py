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


from turtle import Screen, Turtle


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


turtle = Turtle()


def draw_square(side_pixels):
    """Use to draw a square using Turtle graphics."""
    # Ensure pen is down
    turtle.pendown()
    for side in range (4):
        turtle.forward(side_pixels) # Draw a side with length "side_pixels"
        turtle.left(90) # Turn 90 degrees
    # Move cursor to end "right" position of square
    turtle.penup()
    turtle.forward(side_pixels)


def move_next(space):
    """Use to move the cursor."""
    # Ensure pen is up
    turtle.penup()
    turtle.forward(space)


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 05, Turtle graphics.'
          '\nFunction: ',
          main.__name__, sep = '')
    screen = Screen()
    # press_continue()

    # Exercise 1: Function that draws a square with length of side
    # as parameter.
    side_square = 200
    draw_square(side_square)

    # Exercise 2: Move cursor, then draw one more square
    new_space = side_square / 2
    move_next(new_space)
    draw_square(side_square)


    # Allow the window to stay until user close it
    screen.mainloop()
    press_exit()


if __name__ == "__main__":
    main()
