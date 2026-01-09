"""Module for Lesson 02, Week 05, Exercise 02.

Parts 2.1 through 2.4, functions.
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


def c_to_f(degree):
    """Use to convert degree Celsius to Fahrenheit.

    Will return None if input is less than
    the absolute zero.
    Note this will not handle input that differ from int or float.
    Going by exercise for this, will not add difficulty or
    functionality at this time.
    """
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32
