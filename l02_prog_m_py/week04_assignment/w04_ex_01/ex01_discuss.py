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
    print('\nShould print out:\ntest')
    press_continue()
    # # Defines the function foo which takes an argument t.
    # # However, t is never used, function prints test, always.
    # # Will need to change to pass pylint.
    # def foo(t):
    #     """Use for 1a exercise to print."""
    #     print('test')
    #
    # # Calls function foo with hej as t, though not actually used.
    # # Will need to change to pass pylint.
    # foo('hej')

    # Pylint fixes
    # 1) "foo" is a disallowed name
    # 2) t is an unused argument
    def foo_1a():
        """Use for foo_1a, print only."""
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
    print('\nShould print out:\n3 5')
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
    print('\nShould print out:\n15')
    press_continue()
    # Defines a function that takes two arguments
    # Returns the two arguments multiplied
    def fun1(x, y):
        """Use for fun1 function, return multiplied."""
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
    print('\nShould print out:\n125')
    press_continue()
    # Defines a function that takes one argument
    # Returns the argument multiplied with 5
    def fun2(i):
        """Use for fun2 function, return multiplied by 5."""
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
    print('\nShould print out:\n7')
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
    print('\nShould print out:\n18')
    press_continue()

    # # Original code start
    # # Defines a function foo, which takes an argument named "i"
    # # Returns 2 multiplied with i squared
    # def foo(i):
    #     """Use for foo, return 2 multiplied with i^2."""
    #     return 2 * i * i
    #
    # # Defines a function goo, which takes two arguments, "x" and "y"
    # # x is a function name, y an argument
    # # Returns the value from the function call
    # def goo(x, y):
    #     """Use for goo function."""
    #     return x(y)
    #
    # #a = goo(foo, 3); # Should not have a semicolon
    # # "a" is assigned goo function call, using foo as x and 3 as y
    # # foo is called with 3, resulting in 2 * 3 * 3 = 18
    # # "a" gets the value of 18
    # a = goo(foo, 3)  # Removed semicolon
    # # Will print 18
    # print(a)
    # # Original code end

    # Code to print out 18

    def foo_1f(i):
        """Use for foo_1f, return 2 multiplied with i^2."""
        return 2 * i * i

    def goo_1f(x, y):
        """Use for goo_1f, return function call result."""
        return x(y)

    a = goo_1f(foo_1f, 3)
    print(a)

    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1f


def w04_ex01_g():
    """Use for 1g."""
    print('This is part 1g.\nFunction: ',
          w04_ex01_g.__name__, sep='')
    print('\nShould print out:\nTrue\nTrue')
    press_continue()

    # # Original code start
    # # Function is_number returns True if either an int or a float
    # # is used as an argument during the function call
    # # Yes, it can be improved!
    # # The elif is not needed, since the above line returns something
    # # Also, you do not know if it was an int or float, this can be
    # # Added as a printout, if wanted.
    # def is_number(x):
    #     if isinstance(x, int):
    #         return True
    #     elif isinstance(x, float):
    #         return True
    #     return False
    #
    # # Prints: True
    # print(is_number(5.5))
    # # Prints: True
    # print(is_number(42))
    # # Original code end

    def is_number(x):
        """Use to check if int or float, or not."""
        if isinstance(x, int):
            #print('An integer was sent in.')
            return True
        if isinstance(x, float):
            #print('A floating point number was sent in.')
            return True
        print('Neither int, nor float, was passed to the function.')
        return False

    # Prints: True
    print(is_number(5.5))
    # Prints: True
    print(is_number(42))
    # # Test use
    # print(is_number('a'))

    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1g


def w04_ex01_h():
    """Use for 1h."""
    print('This is part 1h.\nFunction: ',
          w04_ex01_h.__name__, sep='')
    print('\nShould not really do anything.')
    press_continue()

    # Original code start
    # Function average_words, takes an argument "strings"
    def average_words(strings):
        """Use to check some word lengths, return selection."""
        # Empty list
        found = []
        # For loop over the input argument
        for item in strings:
            # If the "item" has more than 4, but less than 8 length
            # ["how's", 'going', 'coding']
            if 4 < len(item) < 8:
                # Append "item" to list
                found.append(item)
        # Return the list
        return found

    # Call to function with some words in a list,
    # but does not store the result.
    # Nothing will print, nor be stored, dummy feature.
    average_words(["sup", "how's", "it", "going", "reflecting", "on",
                   "programs", "and", "coding"])
    # Original code end

    # # Attempt to do something
    # words_1h = average_words(["sup", "how's", "it", "going", "reflecting", "on",
    #                "programs", "and", "coding"])
    # print(words_1h)

    print('End of 1h.')
    press_continue()
    # Yes, I got the result I expected from 1h


def w04_ex01_i_1_and_2():
    """Use for 1i."""
    print('This is part 1i.\nFunction: ',
          w04_ex01_i_1_and_2.__name__, sep='')
    print('\nWill print:\n-11\n0\n0')
    press_continue()

    # Original code start
    # Function that based on name finds the smallest number
    # from the input argument "numbers".
    def find_min(numbers):
        """Use to find the smallest number."""
        # Start with a counter at 0 (bad name, does not count).
        counter = 0
        # Loop over the input argument
        for item in numbers:
            # Check if the number is smaller than counter,
            # which starts at 0 (positive numbers will not work).
            if item < counter:
                # If smaller (negative number) found, assign counter
                # to number found.
                counter = item
        # Prints what is found to be the smallest (negative) item.
        # Else will print default 0, even if not input.
        print(f"The smallest item is: {counter}")
        # Return the found value
        return counter

    # Input list, -11 should be the smallest
    find_min([10, 3, -4, -11])
    # Empty list, 0 will be reported.
    find_min([])
    # Only contains 100, 0 will be reported.
    find_min([100])
    # Original code end

    print()
    ask_y_or_n()
    press_continue()
    # Yes, I got the result I expected from 1i


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
    #w04_ex01_f() # Will print: 18
    #w04_ex01_g() # Will print: True (newline) True
    #w04_ex01_h() # Will not really do anything
    w04_ex01_i_1_and_2()


    press_exit()


if __name__ == "__main__":
    main()
