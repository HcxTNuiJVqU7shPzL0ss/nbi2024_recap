"""Module for tests, L02, W04, Ex02.2, part a."""

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
from ..ex02_functions import (ex02_02a_echo_twice)
# pylint: enable=import-error


def test_ex02_02a_echo_twice__correct_print():
    """Used for unit test of function ex02_02a_echo_twice.

    Check for correct printout.
    """
    use_for_echo2 = 'echo'
    expected = use_for_echo2 * 2
    assert ex02_02a_echo_twice(use_for_echo2) == expected


def test_ex02_02a_echo_twice__not_string():
    """Used for unit test of function ex02_02a_echo_twice.

    Check that sending in different argument than
    str to parameter returns None.
    """
    use_int = 42
    use_float = 42.42
    use_list = ['42']
    use_tuple = ('42', '42')
    check_list = [use_int, use_float, use_list, use_tuple]
    for check in check_list:
        assert ex02_02a_echo_twice(check) is None
