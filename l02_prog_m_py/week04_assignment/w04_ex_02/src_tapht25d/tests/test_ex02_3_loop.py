"""Module for tests, L02, W04, Ex02.3."""

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
from ..ex02_functions import (ex02_03_end_loop)
# pylint: enable=import-error


def test_ex02_03_end_loop__correct_print():
    """Used for unit test of function ex02_03_end_loop.

    Check for correct return value, shall be 32.
    """
    expected = 32
    assert ex02_03_end_loop() == expected
