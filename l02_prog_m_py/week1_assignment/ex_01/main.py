"""Module for 'Hello World'."""


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


MY_NAME = 'Jan (gnoff)'


def press_exit():
    """Use to prompt user to hit enter to continue."""
    input('Press Return (Enter) to exit.\n')


# Print "Hello world"
print('\nHello world')

# Print a welcome message
print('This program was made by', MY_NAME, '\n')


press_exit()
