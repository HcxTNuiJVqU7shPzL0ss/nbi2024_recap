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


import emoji


class Player:
    """Use for Class Player."""

    def __init__(self, x, y):
        """Use to create an object of Player."""
        self.pos_x = x
        self.pos_y = y
        self.score = 0
        self.inventory = []
        self.use_neg = False


    def print_status(self, game_grid):
        """Use to display the board grid and number of points."""
        print(f'\n>>> {emoji.emojize(':strawberry:')} '
              f'Fruit Loop {emoji.emojize(':watermelon:')} <<<')
        print('--------------------------------------\n')
        print(f'You have {self.score} points.\n')
        print(game_grid)


    def set_lava_handling(self, lava_neg):
        """Use to handle lava score reduction.

        Checks if 0 shall be the lowest allowed score,
        or if (unlimited) negative values are allowed.
        """
        self.use_neg = lava_neg


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

        # Return True if no wall is found
        if check_wall in (grid.wall, grid.unstable_wall):
            print('\nNot allowed to walk through walls!')
            input('Press Enter to continue!')
            return False
        return True


    def handle_lava_score(self):
        """Use to handle score for The Floor is Lava."""
        # Handle "The Floor is Lava"
        # Exam Version 1: G (Lose 1 point per step)
        self.score -= 1
        # If gamer has opted to not allow score below 0,
        # Ensure this happens
        if not self.use_neg and self.score < 0:
            self.score += 1


    def move_happening(self, x, y, g, item):
        """Use to check if something happens when player move.

        Check if an item is picked up, and if so add to
        inventory, plus print info to user.
        Also handles "The Floor is Lava" score reduction.
        """
        # Only check if player picked something up, and only
        # move player, if possible to move
        if self.can_move(x, y, g):
            # Check if there is an item on coordinates
            maybe_item = g.get(self.pos_x + x,
                               self.pos_y + y)
            # Move player
            self.move(x, y)

            # # Handle "The Floor is Lava"
            # # Exam Version 1: G (Lose 1 point per step)
            # self.score -= 1
            # # If gamer has opted to not allow score below 0,
            # # Ensure this happens
            # if not self.use_neg and self.score < 0:
            #     self.score += 1
            self.handle_lava_score()

            # Check if there is something to pick up
            if isinstance(maybe_item, item):
                print('')
                # we found something, handle score
                if maybe_item.symbol != 't':
                    self.score += maybe_item.value
                    print(f"You found a {maybe_item.name}, "
                          f"+{maybe_item.value} points.")
                    # Clear the picked up item on board
                    g.clear(self.pos_x, self.pos_y)
                    # Exam Version 1: E (Added to inventory)
                    self.inventory.append(maybe_item.name)
                else:
                    print(f'Oh no, you found a {maybe_item.name}!\n'
                          f'You lost {maybe_item.value} points.')
                    if self.score >= 10 or self.use_neg:
                        self.score += maybe_item.value
                    else:
                        self.score = 0
                print('')
