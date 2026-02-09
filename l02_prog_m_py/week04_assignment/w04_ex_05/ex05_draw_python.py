"""Module for Lesson 02, Week 04, Exercise 05.

Turtle graphics.
Draw: PYTHON
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


import turtle as t
from math import sqrt


letter_height = 100
letter_width = 50
letter_spacing = 10


def move_pen_right_without_drawing(distance):
    t.penup()
    t.setheading(0)
    t.forward(distance)
    t.pendown()


def draw_p():
    """Use to draw the letter P."""
    t.left(90)
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)


def draw_y():
    """Use to draw the letter Y."""
    t.penup()
    t.forward(letter_width/2)
    t.pendown()
    t.left(90)
    t.forward(letter_height/2)
    for i in [1,-1]:
        t.left(i*30)
        scale_factor = 1.11
        t.forward(scale_factor*(letter_height/2))
        t.backward(scale_factor*(letter_height/2))
        t.right(i*30)


def draw_t():
    """Use to draw the letter T."""
    t.penup()
    t.forward(20)
    t.pendown()
    t.left(90)
    t.forward(letter_height)
    t.left(90)
    t.forward(20)
    t.backward(2*20)


def draw_h():
    """Use to draw the letter H."""
    t.left(90)
    t.forward(letter_height)
    t.backward(letter_height/2)
    t.right(90)
    t.forward(letter_width)
    t.left(90)
    t.forward(letter_height/2)
    t.backward(letter_height)


def draw_o():
    """Use to draw the letter O."""
    t.penup()
    t.forward(letter_width/2)
    t.pendown()
    for x in range(12):
        t.forward(letter_width/(12/2))
        t.left(30)


def draw_n():
    """Use to draw the letter N."""
    t.left(90)
    t.forward(letter_height)
    t.right(90 + 60)
    t.forward(sqrt(letter_height**2+letter_width**2))
    t.left(90+60)
    t.forward(letter_height)


def move_pen(letter_number):
    t.penup()
    t.setpos((float(letter_number*(letter_width+letter_spacing)),
              0.0))
    t.setheading(0)
    t.pendown()


def draw_base_lines(length):
    color_previous = t.color()
    t.color("red")
    t.forward(length)
    t.penup()
    t.setposition(0,letter_height)
    t.pendown()
    t.forward(length)
    t.color(color_previous[0], color_previous[1])


def draw_python():
    letters = [draw_p, draw_y, draw_t, draw_h, draw_o, draw_n]
    draw_base_lines(letter_width*(len(letters)+1))

    for i in range(len(letters)):
        move_pen(i)
        letters[i]()
    t.mainloop()
