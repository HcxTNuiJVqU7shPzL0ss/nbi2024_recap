"""Module for Lesson 02, Exam.

Player view.
This contains the Class which creates the player.
Also handles interaction, like movement.
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

    def __init__(self, x, y):
        """Use to create an object of Player."""
        self.pos_x = x
        self.pos_y = y


    def move(self, dx, dy):
        """Use to move the player.

        dx = horizontal movement, from left to right.
        dy = vertical movement, from up to down.
        """
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        """Use to check that you can move.

        # Exam Version 1: C (Player not allowed
        to walk through walls).
        """
        check_x = self.pos_x + x
        check_y = self.pos_y + y
        check_wall = grid.get(check_x, check_y)

        if check_wall in (grid.wall, grid.unstable_wall):
            print('Not allowed to walk through walls!')
            input('Press Enter to continue!')
            return False
        return True


    def move_happening(self, x, y, g, item, inventory, score_in,
                       negative):
        """Use to check if something happens when player move.

        Check if an item is picked up, and if so add to
        inventory, plus print info to user.
        """
        # Only check if player picked something up, and only
        # move player if possible to move
        if self.can_move(x, y, g):
            # Check if there is an item on coordinates
            maybe_item = g.get(self.pos_x + x,
                               self.pos_y + y)
            # Move player
            self.move(x, y)

            # Handle "The Floor is Lava"
            # Exam Version 1: G (Lose 1 point per step)
            score_in -= 1
            # If gamer has opted to not allow score below 0,
            # Ensure this happens
            if not negative and score_in < 0:
                score_in += 1

            # Check if there is something to pick up
            if isinstance(maybe_item, item):
                # we found something, add score
                score_in += maybe_item.value
                print(f"You found a {maybe_item.name}, "
                      f"+{maybe_item.value} points.")
                # Clear the picked up item on board
                g.clear(self.pos_x, self.pos_y)
                # Exam Version 1: E (Added to inventory)
                inventory.append(maybe_item.name)

        return score_in
