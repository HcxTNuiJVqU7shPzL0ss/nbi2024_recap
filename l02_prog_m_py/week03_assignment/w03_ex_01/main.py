"""Module for 'Discuss'.

Lesson 02, Week 03, Exercise 01.
TAP HT 25D.
"""

#####################################################################
# Copyright 2026 gnoff
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


def ex1_part1():
    """Use to handle the code example from part 1.1."""
    # Limit is set to 15
    limit = 15
    # index is set to 2
    index = 5

    print('This is part 1 of exercise 1.\n\n'
          'Should be:\n5\n7\n9\n11\n13\n15')
    press_continue()

    # The while loop runs while limit is equal to or
    # larger then index
    while index <= limit:
        # Print the value of index
        print(index)
        # Increase value of index by 2
        index = index + 2
        # Should be: 5, 7, 9, 11, 13, 15

    print('\nThat was it, part 1 now done.')
    # Yes, it did what I thought it would do.
    press_continue()


def ex1_part2():
    """Use to handle the code example from part 1.2."""
    print('This is part 2 of exercise 1.\n\n'
          'Should be:\n0\n1\n2\n3\n4\n\n6\n7\n8\n9')
    press_continue()

    # Loop from 0 to 9
    for i in range(10):
        # If i == 5, print only a newline
        if i == 5:
            print('')
        # If i != 5, print the number
        else:
            print(i)
            # Should be: 0, 1, 2, 3, 4, newline, 6, 7, 8, 9

        # Increase the value of i with 1
        # However, makes no difference in this loop, not used
        # Should remove this line, the for loop handles it already
        # i = i + 1

    print('\nThat was it, part 2 now done.')
    # Yes, it did what I thought it would do.
    press_continue()


def ex1_part3():
    """Use to handle the code example from part 1.3."""
    print('This is part 3 of exercise 1.\n\n'
          'Should be:\n15')
    press_continue()

    # Start with value 0
    counter = 0
    # Loop from 0 to 5
    for i in range(6):
        # Increase counter with the value for i
        counter += i
    # Print the value
    # Should be 0 + 1 + 2 + 3 + 4 + 5 = 15
    print(counter)

    print('\nThat was it, part 3 now done.')
    # Yes, it did what I thought it would do.
    press_continue()


def ex1_part4():
    """Use to handle the code example from part 1.4."""
    print('This is part 4 of exercise 1.\n\n'
          'Should be:\nx is 145 and y is 10.')
    press_continue()

    # x starts at 0
    x = 0
    # y starts at 1
    y = 1
    # Loops while y is less than 10
    while y < 10:
        # If y is even, decrease x with the value of y
        if y % 2 == 0:
            x -= y  # Tips: sätt en brytpunkt här
        # If y is odd, increase x with the value of y squared
        else:
            x += y * y  # och här
        # Increase the value of y by 1
        y += 1

    # y = 1 --> x = 0 + 1 --> x = 1
    # y = 2 --> x = x - 2 --> x = 1 - 2 --< x = -1
    # y = 3 --> x = x + 9 --> x = 8
    # y = 4 --> x = 8 - 4 --> x = 4
    # y = 5 --> x = 4 + 25 = 29
    # y = 6 --> x = 29 - 6 --> x = 23
    # y = 7 --> x = 23 + 49 --> x = 72
    # y = 8 --> x = 72 - 8 = 64
    # y = 9 --> x = 64 + 81 --> x = 145
    # y = 10 --> while loop ends, x is still

    # Nothing is actually printed,though the question
    # is what gets printed?
    # Either it has been missed, or the question is
    # what the value of x, and maybe y, is at the end
    print(f'In the end, x is {x}, and y is {y}')

    print('\nThat was it, part 4 now done.')
    # Yes, it did what I thought it would do, at least
    # when adding print out to check the answer
    # Else also yes, nothing got printed...
    press_continue()


def ex1_part5():
    """Use to handle the code example from part 1.5."""
    print('This is part 5 of exercise 1.\n\n'
          'Should be first:\n_tim')
    press_continue()
    message = 'its_time_to_get_coding'
    print(message[3:7])

    press_continue()
    print('This is still part 5 of exercise 1.\n\n'
          'Now, with changes, should be:\ntime\n')
    message = 'its_time_to_get_coding'
    print(message[4:8])

    print('\nThat was it, part 5 now done.')
    # Yes, it did what I thought it would do
    press_continue()


def main():
    """Use as module for Main.

    This version made for 2025 (and 2026), TAP HT 25D.
    Discuss the purpose of the code.
    Write down what you think will be printed.
    Type the code into your IDE, exactly as stated.
    Run it.
    """
    print('\nThis is exercise 1, "Discuss", from week 3.')
    press_continue()

    # ex1_part1()
    # ex1_part2()
    # ex1_part3()
    # ex1_part4()
    ex1_part5()

    press_exit()


if __name__ == "__main__":
    main()
