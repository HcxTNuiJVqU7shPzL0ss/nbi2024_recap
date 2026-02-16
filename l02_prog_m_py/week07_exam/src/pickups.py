"""Module for Lesson 02, Exam.

Pickups view.
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


from dataclasses import dataclass


# Use a dataclass since not enough public functions
# as to properly use a "regular" Class
@dataclass
class Item:
    """Use to represent items that can be picked up."""

    def __init__(self, name, value=20, symbol='?'):
        """Use to initialize an object.

        # Exam Version 1: D (Value is 20, not 10)
        """
        self.name = name
        self.value = value
        self.symbol = symbol


    def __str__(self):
        """Use to print."""
        return self.symbol


# Used to randomize OG fruits and veggies
# These give points if/when picked up
pickups = [Item('carrot'), Item('apple'), Item('strawberry'),
           Item('cherry'), Item('watermelon'), Item('radish'),
           Item('cucumber'), Item('meatball')]


def randomize(grid):
    """Use to create random items.

    Place the items on the board grid.
    """
    for item in pickups:
        while True:
            # Randomly generate a position until there is
            # one not previously used
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                # Abort the while loop, continue
                # with the next iteration of the for loop
                break
