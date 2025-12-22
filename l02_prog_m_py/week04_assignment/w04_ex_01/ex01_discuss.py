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
                                            press_exit, ask_y_or_n)


def w04_ex01_a():
    """Use for 1a part."""
    print('This is part 1a.\nFunction: ',
          w04_ex01_a.__name__, sep='')
    print('\nShould print out: test')
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
    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1a


def w04_ex01_b():
    """Use for 1b."""
    print('This is part 1b.\nFunction: ',
          w04_ex01_b.__name__, sep='')
    print('\nShould print out: 3 5')
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
    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1b


def w04_ex01_c():
    """Use for 1c."""
    print('This is part 1c.\nFunction: ',
          w04_ex01_c.__name__, sep='')
    print('\nShould print out: 15')
    press_continue()
    # Defines a function that takes two arguments
    # Returns the two arguments multiplied
    def fun1(x, y):
        return x * y

    # Prints 15
    print(fun1(3, 5))

    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1c


def w04_ex01_d():
    """Use for 1d."""
    print('This is part 1d.\nFunction: ',
          w04_ex01_d.__name__, sep='')
    print('\nShould print out: 125')
    press_continue()
    # Defines a function that takes one argument
    # Returns the argument multiplied with 5
    def fun2(i):
        return 5 * i

    x = 2
    y = 3
    # First with x returns 2 * 5 = 10
    # Second with y returns 3 * 5 = 15
    # The two are added: 10 + 15 = 25
    # 25 is sent in to be multiplied by 5 = 125
    a = fun2(fun2(x) + fun2(y))
    # 125 to be printed
    print(a)

    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1d


def w04_ex01_e():
    """Use for 1e."""
    print('This is part 1e.\nFunction: ',
          w04_ex01_e.__name__, sep='')
    print('\nShould print out: 7')
    press_continue()

    # # "a" is assigned to 5
    # a = 5
    # # fun3 is defined with one argument
    # # The argument has 1 added to it
    # # Nothing is returned or printed
    # # The function is never called = dead code
    # # Also, "a" is shadowed from outer, likely to confuse
    # # Will need to fix to actually use
    # def fun3(a):
    #     a += 1
    #
    # # 2 is added to , so now 7
    # a += 2
    # # Should print out 7
    # print(a)

    # Code to print out 7
    a = 5
    a += 2
    print(a)
    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1e


def w04_ex01_f():
    """Use for 1f."""
    print('This is part 1f.\nFunction: ',
          w04_ex01_f.__name__, sep='')
    print('\nShould print out: 18')
    press_continue()

    # Original code start
    # Defines a function foo, which takes an argument named "i"
    # Returns 2 multiplied with i squared
    def foo(i):
        return 2 * i * i

    # Defines a function goo, which takes two arguments, "x" and "y"
    # x is a function name, y an argument
    # Returns the value from the function call
    def goo(x, y):
        return x(y)

    #a = goo(foo, 3); # Should not have a semicolon
    # "a" is assigned goo function call, using foo as x and 3 as y
    # foo is called with 3, resulting in 2 * 3 * 3 = 18
    # "a" gets the value of 18
    a = goo(foo, 3)  # Removed semicolon
    # Will print 18
    print(a)
    # Original code end

    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1f


def main():
    """Use as main function."""
    print('\nWeek 04, Exercise 01, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    #w04_ex01_a() # Will print: test
    #w04_ex01_b() # Will print: 3 5
    #w04_ex01_c() # Will print: 15
    #w04_ex01_d() # Will prin: 125
    #w04_ex01_e() # Will print: 7
    w04_ex01_f()


    press_exit()


if __name__ == "__main__":
    main()
