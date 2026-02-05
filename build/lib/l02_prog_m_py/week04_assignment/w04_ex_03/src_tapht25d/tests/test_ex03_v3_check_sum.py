"""Module for tests, L02, W04, Ex03, version 3.

Check sum calculation.
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
from ..ex03_functions import ex03_v3_check_sum
# pylint: enable=import-error


def test_ex03_v3_check_sum__check_card():
    """Use for unit test of function ex03_v3_check_sum.

    Will check that the returned sum is correct.
    """
    sum_before = 13
    new_card = 13
    sum_after = ex03_v3_check_sum(sum_before, new_card)
    check_sum_correct = 26
    assert sum_after == check_sum_correct


def test_ex03_v3_check_sum__illegal_sum():
    """Use for unit test of function ex03_v3_check_sum.

    Will check that the sum used cannot be outside the range
    from 0 to 21.
    """
    correct_card_value = 1
    sum_too_low = -1
    sum_too_high = 22
    too_low_return = ex03_v3_check_sum(sum_too_low,
                                       correct_card_value)
    too_high_return = ex03_v3_check_sum(sum_too_high,
                                        correct_card_value)
    assert too_low_return is too_high_return
    assert too_low_return is None


def test_ex03_v3_check_sum__illegal_card():
    """Use for unit test of function ex03_v3_check_sum.

    Will check that the card used cannot be outside the range
    from 1 to 13.
    """
    correct_sum_value = 21
    card_too_low = -1
    card_too_high = 22
    too_low_return = ex03_v3_check_sum(correct_sum_value,
                                       card_too_low)
    too_high_return = ex03_v3_check_sum(correct_sum_value,
                                        card_too_high)
    assert too_low_return is too_high_return
    assert too_low_return is None
