"""Module for ex04, part 1a."""


#####################################################################
# Copyright 2025 gnoff
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


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit,
                                            enter_int_range)


print('\nExercise 4, part 1a.\n')
press_continue()


DISTANCE = 470 # Nr of km between sthlm and gbg
IN_STRING = 'How fast, in km/h, do you want to drive: '

speed_kmh = enter_int_range(IN_STRING, 50, 120, True)

speed_mps = (speed_kmh * 1000) / 3600

nr_of_sec = (DISTANCE * 1000) / speed_mps

print('\nIt will take you', nr_of_sec, 'seconds to drive.')
press_exit()
