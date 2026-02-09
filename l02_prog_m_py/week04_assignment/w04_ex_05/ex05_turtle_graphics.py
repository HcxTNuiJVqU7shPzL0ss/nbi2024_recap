"""Module for Lesson 02, Week 04, Exercise 05.

Turtle graphics.
"""

#####################################################################
# Copyright 2025-2026 gnoff
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


from ex05_draw_python import draw_python

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


def draw_circle(radius):
    """Use to draw a circle."""
    # Ensure pen is down
    turtle.pendown()
    turtle.circle(radius)


def alternate_part03(no_steps, draw_pix, angle):
    """Alternate way of drawing a circle."""
    # Ensure pen is down
    turtle.pendown()
    for x in range(no_steps):
        turtle.forward(draw_pix)
        turtle.right(angle)


def draw_p(p_height):
    """Use to draw the capital P in python."""
    # Ensure pen is down
    turtle.pendown()
    # Point "upwards"
    turtle.left(90)
    # Draw the main leftmost line of P
    turtle.forward(p_height)
    # Draw the half circle of P
    turtle.penup()
    turtle.right(180)
    turtle.forward(int(p_height / 2))
    turtle.left(90)
    # alternate_part03(p_range, p_steps, p_angle)
    turtle.pendown()
    turtle.circle(90, 90)
    turtle.circle(90, 90)


def draw_python_letters():
    """Use to draw the letters: PYTHON."""
    draw_python()


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 05, Turtle graphics.'
          '\nFunction: ',
          main.__name__, sep = '')
    screen = Screen()
    # press_continue()

    turtle.speed(3)

    # draw_python_letters()

    # Part 1: Function that draws a square with length of side
    # as parameter.
    side_square = 200
    draw_square(side_square)
    press_continue()

    # Part 2: Move cursor, then draw one more square.
    new_space = side_square / 2
    move_next(new_space)
    draw_square(side_square)
    press_continue()

    # Part 3: Draw a circle.
    c_radius = side_square / 2
    move_next(new_space * 2)
    draw_circle(c_radius)
    press_continue()

    # Alternate part 3
    # Ensure pen is up
    turtle.penup()
    turtle.clear()
    turtle.home()
    range_3 = 360
    forward_3 = 1
    right_3 = 1
    alternate_part03(range_3, forward_3, right_3)
    press_continue()


    # Draw PYTHON

    # Draw P
    # Ensure pen is up
    turtle.penup()
    turtle.clear()
    turtle.home()
    height_p = 360
    draw_p(height_p)


    # Allow the window to stay until user close it
    screen.mainloop()
    press_exit()


if __name__ == "__main__":
    main()
