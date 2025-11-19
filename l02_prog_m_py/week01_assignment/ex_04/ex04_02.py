"""Module for ex04, part 2."""


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
                                            enter_int)


print('\nExercise 4, part 2.\n')
press_continue()


INTEXT_SIDE1 = 'Enter the length of side 1 of the triangle: '
INTEXT_SIDE2 = 'Enter the length of side 2 of the triangle: '

LOW = 1
HIGH = 99
USE_RANGE = True


side1_i = enter_int(INTEXT_SIDE1, LOW, HIGH, USE_RANGE)

side2_i = enter_int(INTEXT_SIDE2, LOW, HIGH, USE_RANGE)

hypo_sq = (side1_i * side1_i) + (side2_i * side2_i)

hypo = (hypo_sq ** 0.5)

print('')
print(f"The hypotenuse is: {hypo:.2f}")
print('')
press_exit()
