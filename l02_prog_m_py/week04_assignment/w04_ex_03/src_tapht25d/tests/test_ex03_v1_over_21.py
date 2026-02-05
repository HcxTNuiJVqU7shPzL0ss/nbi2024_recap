"""Module for tests, L02, W04, Ex03, version 1."""

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
from ..ex03_functions import ex03_01_find_number
# pylint: enable=import-error


def test_ex03_01_find_number__correct_return():
    """Use for unit test of function ex03_01_find_number.

    Checks that the correct number is returned.
    1 + 2 + 3 + 4 + 5 + 6 = 21
    Hence, 7 should be the number that brings the sum total
    above 21, and the number which is returned.
    """
    correct_bust = 7
    assert ex03_01_find_number() == correct_bust
