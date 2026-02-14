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


@dataclass
class Item:
    """Use to represent items that can be picked up."""

    def __init__(self, name, value=10, symbol="?"):
        """Use to initialize an object."""
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        """Use to print."""
        return self.symbol


pickups = [Item("carrot"), Item("apple"), Item("strawberry"),
           Item("cherry"), Item("watermelon"), Item("radish"),
           Item("cucumber"), Item("meatball")]


def randomize(grid):
    """Use to create random items."""
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                # avbryt while-loopen, fortsätt med nästa varv i for-loopen
                break
