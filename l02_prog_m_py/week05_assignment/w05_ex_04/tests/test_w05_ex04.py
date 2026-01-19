"""Module for tests, L02, W05, Ex04."""

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


from ..src.w05_ex04_functions import multiplication_table


def test_multiplication_table__no_int():
    """Used for unit test of function multiplication_table.

    Test when either n or limit is non integer.
    Checks that empty list is returned.
    Handles ac_001, parts 1 through 4 (all).
    """
    n_ok = 4
    limit_ok = 5
    expected = []
    n_float = 4.2
    assert multiplication_table(n_float, limit_ok) == expected
    n_str = ''
    assert multiplication_table(n_str, limit_ok) == expected
    n_tup = (3, 4)
    assert multiplication_table(n_tup, limit_ok) == expected
    n_list = [1, 2]
    assert multiplication_table(n_list, limit_ok) == expected
    limit_float = 3.14
    assert multiplication_table(n_ok, limit_float) == expected
    limit_str = '4'
    assert multiplication_table(n_ok, limit_str) == expected
    limit_tup = (1, 8)
    assert multiplication_table(n_ok, limit_tup) == expected
    limit_list = [7, 8]
    assert multiplication_table(n_ok, limit_list) == expected
    # Both "wrong"
    assert multiplication_table(n_tup, limit_float) == expected


def test_multiplication_table__pos_int():
    """Used for unit test of function multiplication_table.

    Test that both n and limit are positive integers.
    Checks that empty list is returned if 0 is used.
    Handles ac_002, parts 1 through 2 (all).
    """
    n_zero = 0
    limit_zero = 0
    n_ok = 3
    limit_ok = 2
    expected_zero = []
    assert multiplication_table(n_zero, limit_ok) == expected_zero
    assert multiplication_table(n_ok, limit_zero) == expected_zero
    expected_ok = [3, 6]
    assert multiplication_table(n_ok, limit_ok) == expected_ok


def test_multiplication_table__above_limit():
    """Used for unit test of function multiplication_table.

    Test that both n and limit are within the upper limit.
    Checks that empty list is returned if above 10 is used.
    Handles ac_003, parts 1 through 2 (all).
    """
    n_high = 11
    limit_high = 42
    n_ok = 3
    limit_ok = 2
    expected_high = []
    assert multiplication_table(n_high, limit_ok) == expected_high
    assert multiplication_table(n_ok, limit_high) == expected_high
    expected_ok = [3, 6]
    assert multiplication_table(n_ok, limit_ok) == expected_ok
