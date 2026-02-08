"""Module for tests, L02, W04, Ex04.

Handle unit test of function: deal_poker_hand
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
from ..ex04_functions import deal_poker_hand
# pylint: enable=import-error


def test_deal_poker_hand__correct_values():
    """Use for unit test of function deal_poker_hand.

    Checks that the returned value contains a total
    of 5 cards.
    """
    hand_to_check = deal_poker_hand()
    assert isinstance(hand_to_check, list)
    assert len(hand_to_check) == 5
