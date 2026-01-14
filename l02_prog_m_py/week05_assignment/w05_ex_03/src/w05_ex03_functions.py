"""Module for Lesson 02, Week 05, Exercise 03.

Functions.
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


global_list = [
        'Peter Svensson',
        'Petra Karlsson',
        'Maria Bylund',
        'Marie Hson-Larson',
        'banana',
        'apple',
        'carrot'
    ]


def auto_complete(input_str, master_list):
    """Use to match input_str (str) against master_list.

    Here input_str shall fully match against any item within
    master_list.
    """
    # Not a list used for master_list
    if not isinstance(master_list, list):
        return [None, 'master_list is not a list']
    # Yes, master_list is a list, but includes item(s) not str
    if not all(isinstance(item, str) for item in master_list):
        return [None, 'master_list contain non str item(s)']
    # Empty master_list
    if not master_list:
        return [None, 'master_list is empty']

    return 'this is not implemented'
