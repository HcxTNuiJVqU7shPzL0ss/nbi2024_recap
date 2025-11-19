"""Module for 2a."""


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
                                            press_exit)


print('\nExercise 3, part 2a.\n')
press_continue()

ORIG_PRICE = 2000
DISCOUNT = 50

DISC_PRICE = ORIG_PRICE * (DISCOUNT / 100)

print('\nThe original price was:', ORIG_PRICE)
print('The discount was:', str(DISCOUNT) + '%')
print('Your discounted price is:', DISC_PRICE, '\n')
press_exit()
