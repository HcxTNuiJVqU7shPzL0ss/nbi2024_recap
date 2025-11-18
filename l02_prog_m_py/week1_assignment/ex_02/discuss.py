"""Module for 'Discuss'."""


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


from my_funct_dir.my_base_functions import *


TICKET_PRICE = 100 # Ticket price
FUNDS = 200 # Available funds


# Calculate how much you will have left
MONEY_LEFT = FUNDS - TICKET_PRICE

# Calculate half of what is left
HALF_LEFT = MONEY_LEFT / 2


print('\nThere is', MONEY_LEFT, "SEK over.")
print('Half of what is left over is:', HALF_LEFT, '\n')


press_exit()
