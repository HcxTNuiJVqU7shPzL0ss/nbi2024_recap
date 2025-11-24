"""Module for 'Hello World'.

Lesson 02, Week 01, Exercise 01.
"""

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


from my_funct_dir.my_base_functions import (press_exit)


# #pylint: disable=line-too-long
# # pylint: disable=import-error
# # For some reason pylint will not see it is available to import here
# import sys
# sys.path.insert(0, 'C:\\Users\\rock_\\OneDrive - Acumis Minds AB\\Python-kurs\\PycharmProjects\\nbi2024_recap\\my_funct_dir')
#
# import my_funct_dir.my_base_functions
# from my_funct_dir.my_base_functions import press_exit
# # pylint: enable=import-error
# #pylint: enable=line-too-long

def main():
    """Use as module for Main."""
    my_name = 'Jan (gnoff)'

    # Print "Hello world"
    print('\nHello world')

    # Print a welcome message
    print('This program was made by', my_name, '\n')

    #my_base_functions.press_exit()
    press_exit()


if __name__ == "__main__":
    main()
