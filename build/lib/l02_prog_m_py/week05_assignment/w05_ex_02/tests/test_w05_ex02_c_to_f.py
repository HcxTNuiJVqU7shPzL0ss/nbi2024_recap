"""Module for tests, L02, W05, Ex02.

Handling unit test of function: c_to_f.
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


from ..src.w05_ex02_functions import c_to_f


def test_c_to_f__too_cold():
    """Used for unit test of function c_to_f.

    Check if below absolute zero, result shall be None.
    """

    expected = None
    actual = c_to_f(-300)
    assert actual == expected
    actual = c_to_f(-273.16)
    assert actual == expected


def test_c_to_f__check_temps():
    """Used for unit test of function c_to_f.

    Check if at absolute zero or higher.
    """

    assert round(c_to_f(-273.15), 2) == -459.67
    assert c_to_f(0) == 32
    assert c_to_f(-40) == -40
    assert c_to_f(1000) == 1832
