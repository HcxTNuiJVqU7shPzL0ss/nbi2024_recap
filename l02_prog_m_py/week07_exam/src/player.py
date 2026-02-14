"""Module for Lesson 02, Exam.

Player view.
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


class Player:
    """Use for Class Player."""

    marker = "@"

    def __init__(self, x, y):
        """Use to create object."""
        self.pos_x = x
        self.pos_y = y

    # Move the player, "dx" and "dy" is the difference
    def move(self, dx, dy):
        """Use to oves the player.

        dx = horizontal movement, from left to right.
        dy = vertical movement, from up to down.
        """
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        """Use to check that you can move."""
        check_x = self.pos_x + x
        check_y = self.pos_y + y
        check_wall = grid.get(check_x, check_y)

        if check_wall == grid.wall:  # "■":
            print('Not allowed to walk through walls!')
            input('Press Enter to continue!')
            return False
        return True
