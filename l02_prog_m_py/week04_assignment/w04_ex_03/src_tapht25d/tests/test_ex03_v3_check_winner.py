"""Module for tests, L02, W04, Ex03, version 3.

Check who won, user or computer.
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
from ..ex03_functions import ex03_v3_check_winner
# pylint: enable=import-error


def test_ex03_v3_check_winner__check_tie():
    """Use for unit test of function ex03_v3_check_winner.

    Will check that tie was called correctly.
    """
    expected = 'tie'
    user_score = 13
    computer_score = 13
    winner_tie = ex03_v3_check_winner(user_score, computer_score)
    assert winner_tie == expected


def test_ex03_v3_check_winner__check_user():
    """Use for unit test of function ex03_v3_check_winner.

    Will check that the user is correctly returned as winner.
    """
    expected = 'user'
    user_score = 21
    computer_score = 3
    winner_user = ex03_v3_check_winner(user_score, computer_score)
    assert winner_user == expected


def test_ex03_v3_check_winner__check_computer():
    """Use for unit test of function ex03_v3_check_winner.

    Will check that the computer is correctly returned as winner.
    """
    expected = 'computer'
    user_score = 2
    computer_score = 5
    winner_computer = ex03_v3_check_winner(user_score,
                                           computer_score)
    assert winner_computer == expected


def test_ex03_v3_check_winner__check_illegal_score():
    """Use for unit test of function ex03_v3_check_winner.

    Will check that the score used cannot be outside the range
    from 0 to 21.
    """
    expected = None
    user_score = 21
    computer_score = 3
    illegal_score_low = -1
    illegal_score_high = 22
    winner_illegal = ex03_v3_check_winner(illegal_score_low,
                                          computer_score)
    assert winner_illegal == expected
    winner_illegal = ex03_v3_check_winner(illegal_score_high,
                                          computer_score)
    assert winner_illegal == expected
    winner_illegal = ex03_v3_check_winner(user_score,
                                          illegal_score_low)
    assert winner_illegal == expected
    winner_illegal = ex03_v3_check_winner(user_score,
                                          illegal_score_high)
    assert winner_illegal == expected
