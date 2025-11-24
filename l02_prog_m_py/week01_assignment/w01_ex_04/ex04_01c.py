"""Module for ex04, part 1c."""

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


# pylint: disable=import-error
# For some reason pylint will not see it is available to import here
#from ex04_01a import stockholm_gbg_main
import ex04_01a
# pylint: enable=import-error


from my_funct_dir.my_base_functions import (press_continue,
                                            press_exit)


def conv_sec(nr_of_seconds):
    """Convert seconds.

    From seconds into whole hours and minutes.
    """
    nr_of_hours = nr_of_seconds // 3600 # How many hours
    nr_of_seconds %= 3600 # Remaining seconds
    nr_of_minutes = nr_of_seconds // 60 # How many minutes
    nr_of_seconds %= 60 # Remaining seconds

    # pylint: disable=consider-using-f-string
    return "%d:%02d:%02d" % (nr_of_hours, nr_of_minutes,
                             nr_of_seconds)
    # pylint: enable=consider-using-f-string


def main():
    """Use as Main for ex 04, part 01c."""
    print('\nExercise 4, part 1c.\n')
    press_continue()

    # nr_of_sec = stockholm_gbg_main()
    nr_of_sec = ex04_01a.stockholm_gbg_main()

    result = conv_sec(nr_of_sec)

    split_result = result.split(':')

    formatted = ''
    for i, split_result in enumerate(split_result):
        if i == 0:
            add_this = ' h, '
        elif i == 1:
            add_this = ' min, '
        else:
            add_this = ' sec'
        formatted = formatted + split_result + add_this

    print('\nIt will take you:', formatted, 'to drive.')
    press_exit()


if __name__ == '__main__':
    main()
