"""Module for 'Date today'.

Lesson 02, Week 01, Exercise 04, Part 03a.
Done "off course".
"""

#####################################################################
# Copyright 2025-2026 gnoff
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


from datetime import date

from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


print('\nExercise 4, part 3a.')
press_continue()

print('The date today is:', date.today())

press_exit()
