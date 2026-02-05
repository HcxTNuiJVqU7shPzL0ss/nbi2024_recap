"""Module for tests, L02, W04, Ex02, part 2a."""

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
from ..ex02_functions import ex02_02a_echo_twice
# pylint: enable=import-error


def test_ex02_02a_echo_twice__correct_print():
    """Used for unit test of function ex02_02a_echo_twice.

    Check for correct printout.
    """
    use_for_echo2 = 'echo'
    expected_1 = use_for_echo2 * 2
    expected_2 = 'echoecho'
    expected_list = [expected_1, expected_2]
    for expected in expected_list:
        assert ex02_02a_echo_twice(use_for_echo2) == expected


def test_ex02_02a_echo_twice__not_string():
    """Used for unit test of function ex02_02a_echo_twice.

    Check that sending in different argument than
    str to parameter returns None.
    """
    use_int_02a = 42
    use_float_02a = 42.42
    use_list_02a = ['42']
    use_tuple_02a = ('42', '42')
    check_list_02a = [use_int_02a, use_float_02a, use_list_02a,
                      use_tuple_02a]
    for check_02a in check_list_02a:
        assert ex02_02a_echo_twice(check_02a) is None
