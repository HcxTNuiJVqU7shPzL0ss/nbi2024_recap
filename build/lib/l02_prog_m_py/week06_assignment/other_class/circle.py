"""Module for 'Circle'.

Example from: https://realpython.com/python-classes/
Done "off course".
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


import math


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


# Keyword class is used to define the class Circle
class Circle:
    """Use as class when creating an object of a circle."""

    def __init__(self, radius, name):
        """Use as method to initialize an object.

        Defines and sets the initial values for the object's
        attributes.
        The first argument self holds a reference to the current
        object, so it can be used inside the class.
        """
        self.radius = radius
        self.name = name

    def calculate_area(self):
        """Use to compute the area of a circle.

        Math module is used to access the pi constant.
        The first argument self holds a reference to the current
        object, so it can be used inside the class.
        """
        area =  math.pi * self.radius ** 2
        return area

    def __str__(self):
        """Use to create human-readable output.

        This has been added to avoid pylint warning.
        Not part of example, they use too few public methods.
        """
        # Rounding is made on my own
        return (f'The {self.name} circle\'s area is: '
                f'{self.calculate_area():.2f}')


def handle_circle_objects():
    """Use to create and then access circle objects."""
    print('Creating your circles.')
    list_of_circles = []
    # Call the Circle() class constructor with parentheses
    # and argument, in this case radius (as in __init__)
    # Create one unique object
    circle_1 = Circle(42, 'First')
    list_of_circles.append(circle_1)
    # Create a different unique object
    circle_2 = Circle(7, 'Second')
    list_of_circles.append(circle_2)

    press_continue()

    print_circle_object_str(list_of_circles)

    press_continue()

    display_circle_radius(list_of_circles)

    press_continue()

    display_circle_area(list_of_circles)

    press_continue()

    # Change the radius value of the first circle
    # The object's internal state or data changes
    print(f'Time to change the radius of the {circle_1.name} '
          f'circle.')
    circle_1.radius = 100
    print(f'The area is now: {circle_1.calculate_area()}')


def print_circle_object_str(print_list):
    """Use to access the str part from an object."""
    print('Printing your circle object\'s str values.\n')
    # Not part of the example, use the __str__ part
    # print(circle_1)
    # print(circle_2)
    for circle in print_list:
        print(circle)


def display_circle_radius(radius_list):
    """Use to access the attribute for radius and print it."""
    print('Printing your circle object\'s radius values.\n')
    # # Access the .radius attribute for the first object
    # print('Circle 1 radius is:', circle_1.radius)
    # # Access the .radius attribute for the second object
    # print('Circle 2 radius is:', circle_2.radius)
    for circle in radius_list:
        print(f'Circle {circle.name} has the radius '
              f'{circle.radius}.')


def display_circle_area(area_list):
    """Use to calculate and display area.

    Call method and calculate area.
    """
    print('Calculating and printing the area of your circle\'s.\n')
    # # Call the .calculate_area() method to calculate the
    # # area of the first circle
    # print('Circle 1 area (not rounded) is:',
    #       circle_1.calculate_area())
    # # And again for the second object
    # print('Circle 2 area (not rounded) is:',
    #       circle_2.calculate_area())
    for circle in area_list:
        print(f'Circle {circle.name} has the area of '
              f'{circle.calculate_area()}')


def main():
    """Use as module for Main.

    This version made for standalone work.
    Not part of the explanation in mentioned site.
    """
    print('\nWorking with classes.')
    press_continue()

    handle_circle_objects()

    press_exit()


if __name__ == "__main__":
    main()
