"""Module for tests, L02, W04, Ex02, part 1."""

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
from ..ex02_functions import (ex02_01_hacker)
# pylint: enable=import-error


def test_ex02_01_hacker__correct_print():
    """Used for unit test of function ex02_01_hacker.

    Check for correct printout.
    """
    use_name = 'gnoff'
    fuse_string = ' is a real hacker'
    expected = use_name + fuse_string
    assert ex02_01_hacker(use_name) == expected


def test_ex02_01_hacker__not_string():
    """Used for unit test of function ex02_01_hacker.

    Check that sending in different argument than
    str to parameter returns None.
    """
    use_int_01 = 42
    use_float_01 = 42.42
    use_list_01 = ['42']
    use_tuple_01 = ('42', '42')
    check_list_01 = [use_int_01, use_float_01, use_list_01,
                     use_tuple_01]
    for check_01 in check_list_01:
        assert ex02_01_hacker(check_01) is None
