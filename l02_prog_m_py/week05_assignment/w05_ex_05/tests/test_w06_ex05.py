"""Module for tests, L02, W05, Ex05."""

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


from ..src.w05_ex05_functions import balance_lists


def test_balance_lists__not_list():
    """Used for unit test of function balance_lists.

    Test when either input is not an actual list.
    Checks that None is returned.
    Handles ac_001, parts 1 through 4 (all).
    """
    expected = []
    assert balance_lists(['a'], ['b']) == expected
