"""Module for tests, src file: player."""

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
from ..src.player import Player
# pylint: enable=import-error


p = Player(0, 0) # Supply x and y


def test_print_status__dummy_values(capsys):
    """Use to run simple test of print_status.

    Use capsys to capture stdout/stderr output.
    Test Player method "print_status"
    """
    # p = Player(0, 0) # Supply x and y
    p.print_status(game_grid='dummy') # Dummy for print

    captured = capsys.readouterr()
    output = captured.out

    # Test that first print happens
    assert 'Fruit Loop' in output
    # Second print
    assert '------------' in output
    # Two asserts for the third print
    assert 'You have 0 points' in output
    assert 'You have used 0 moves' in output
    # Test fourth / last (dummy) print
    assert 'dummy' in output


def test_lava_handling__false():
    """Use to check setting negative values to False.

    Test Player method "lava_handling"
    """
    expected = False
    p.set_lava_handling(lava_neg=expected)
    actual = p.use_neg
    assert actual == expected


def test_lava_handling__true():
    """Use to check setting negative values to True.

    Test Player method "lava_handling"
    """
    expected = True
    p.set_lava_handling(lava_neg=expected)
    actual = p.use_neg
    assert actual == expected


def test_move__x1_y2():
    """Use to simulate move to x=1 and y=2.

    Test Player method "move"
    """
    # Check default is at 0 for both
    assert p.pos_x == 0
    assert p.pos_y == 0
    # Change coordinates
    expected_x = 1
    expected_y = 2
    p.move(dx=expected_x, dy=expected_y)
    # Check that change happened
    assert p.pos_x == expected_x
    assert p.pos_y == expected_y
