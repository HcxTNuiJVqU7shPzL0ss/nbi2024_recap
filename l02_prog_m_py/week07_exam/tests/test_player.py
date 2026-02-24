"""Module for tests, src directory file: player."""

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


X_START = 0
Y_START = 0
GRACE_START = 0
SCORE_START = 0
NEG_START = False

p = Player(x=X_START, y=Y_START) # Supply x and y


def test_print_status__dummy_values(capsys):
    """Use to run simple test of print_status.

    Use capsys to capture stdout/stderr output.
    Test Player method "print_status"
    """
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
    assert actual is expected

    # Reset to default
    p.set_lava_handling(lava_neg=NEG_START)
    actual = p.use_neg
    assert actual is NEG_START


def test_move__x1_y2():
    """Use to simulate move to x=1 and y=2.

    Test Player method "move"
    """
    # Check default is at 0 for both
    assert p.pos_x == X_START
    assert p.pos_y == Y_START

    # Change coordinates
    expected_x = 1
    expected_y = 2
    p.move(dx=expected_x, dy=expected_y)
    # Check that change happened
    assert p.pos_x == expected_x
    assert p.pos_y == expected_y

    # Reset to default
    p.move(dx=-expected_x, dy=-expected_y)
    # Check that change happened
    assert p.pos_x == X_START
    assert p.pos_y == Y_START


def test_handle_lava_score__no_grace_no_negative_default(capsys):
    """Use to test Player metod handle_lava_score.

    No grace period.
    Negative values are not allowed.
    Default "start" values.
    """
    # Check default
    assert p.grace_cnt == GRACE_START
    assert p.score == SCORE_START
    assert p.use_neg is False

    # Call the method without finding an item
    p.handle_lava_score(grace=False)

    # Check grace_cnt and score still at 0
    assert p.grace_cnt == GRACE_START
    assert p.score == SCORE_START

    captured = capsys.readouterr()
    output = captured.out

    # Test that print happens
    assert 'is at 0' in output


def test_handle_lava_score__yes_grace_yes_negative_fake_score(capsys):
    """Use to test Player method handle_lava_score.

    Yes, grace period.
    Yes, negative values allowed.
    Fake score.
    """
    grace_set = 5
    fake_score_set = 1
    # Call the method when finding an item
    p.handle_lava_score(grace=True)

    # Check that grace_cnt is now at 5
    assert p.grace_cnt == grace_set

    captured = capsys.readouterr()
    output = captured.out

    # Test that print happens
    assert 'is at 5' in output


    # Change to allow negative values, and fake a score
    p.use_neg = True
    p.score = fake_score_set

    for i in range(1, 6):
        # Call the method without finding an item
        p.handle_lava_score(grace=False)

        # Check that grace_cnt decreases
        assert p.grace_cnt == grace_set - i
        # Check that score does not decrease
        assert p.score == fake_score_set

        captured = capsys.readouterr()
        output = captured.out

        # Test that print happens
        assert f'is at {p.grace_cnt}' in output

    for i in range(1, 3):
        # With grace_cnt now at 0, check that score decrease
        p.handle_lava_score(grace=False)
        assert p.score == fake_score_set - i
        print(p.score)

    # Back to default
    p.score = SCORE_START
    p.grace_cnt = GRACE_START
    p.use_neg = NEG_START
