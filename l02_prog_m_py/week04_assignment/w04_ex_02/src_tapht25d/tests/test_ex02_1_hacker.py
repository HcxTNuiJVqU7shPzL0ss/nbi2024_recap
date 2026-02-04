"""Module for tests, L02, W04, Ex02.1."""

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


from ..ex02_functions import (ex02_01_hacker)


def test_w04_ex02_1__correct_print():
    """Used for unit test of function ex02_01_hacker.

    Check for correct printout.
    """
    use_name = 'gnoff'
    fuse_string = ' is a real hacker'
    expected = use_name + fuse_string
    assert ex02_01_hacker(use_name) == expected
