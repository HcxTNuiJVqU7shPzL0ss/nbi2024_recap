"""Module for Lesson 02, Week 04, Exercise 01, Discuss."""

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


def w04_ex01_a():
    """Use for 1a."""
    print('This is part 1a.\nFunction: ',
          w04_ex01_a.__name__, sep='')
    press_continue()
    # # Defines the function foo which takes an argument t.
    # # However, t is never used, function prints test, always.
    # # Will need to change to pass pylint.
    # def foo(t):
    #     print('test')
    #
    # # Calls function foo with hej as t, though not actually used.
    # # Will need to change to pass pylint.
    # foo('hej')

    # Pylint fixes
    # 1) "foo" is a disallowed name
    # 2) t is an unused argument
    def foo_1a():
        print('test')

    foo_1a()
    press_continue()
    # Yes, I got the result I expected from 1a


def w04_ex01_b():
    """Use for 1b."""
    print('This is part 1b.\nFunction: ',
          w04_ex01_b.__name__, sep='')
    press_continue()
    # # Defines a function that takes two arguments
    # # Returns the two arguments multiplied
    # def fun1(x, y):
    #     return x * y
    #
    # # Prints 3 and 5
    # # Function is never called, only defined
    # print(3, 5)

    # Fixed as to not have warnings, etc.
    print(3, 5)
    press_continue()
    # Yes, I got the result I expected from 1b


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 01, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    #w04_ex01_a() # Will print: test
    w04_ex01_b()  # Will print: 3 5


    press_exit()


if __name__ == "__main__":
    main()
