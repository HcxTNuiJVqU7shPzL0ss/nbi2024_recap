"""Module for Lesson 02, Exam.

Main view.
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


# pylint: disable=import-error
from grid import Grid
from player import Player

import pickups

from display_status import print_status
# pylint: enable=import-error


# Set the player start position in the middle of the board
player = Player(x = 18, y = 6)
# Set player start score (0 when starting)
score = 0
# Create the player inventory (empty at start)
inventory = []

# Create board
g = Grid(player)
# Place player on the board
g.set_player(player)
# Create walls around the board
g.make_walls()
# Randomly create and place items on board
pickups.randomize(g)


# List of acceptable commands, not including q, x, i, h
player_commands = ['a', 's', 'd', 'w']

# List of exit commands
exit_commands = ['q', 'x']

# Default values
command = 'a'

# Loop until user enters Q or X
while not command.casefold() in ['q', 'x']:
    print_status(g)

    command = input('Use WASD to move, Q/X to quit. ')
    command = command.casefold()[:1]

    if command == 'd' and player.can_move(1, 0, g):  # move right
        # skapa funktioner, så vi inte behöver upprepa så mycket
        # kod för riktningarna "W, A, S"
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
