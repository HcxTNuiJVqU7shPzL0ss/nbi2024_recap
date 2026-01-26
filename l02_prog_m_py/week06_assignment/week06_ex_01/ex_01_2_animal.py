"""Module for 'Discuss'.

Lesson 02, Week 06, Exercise 01, parts 2a and 2b.
Done "off course".
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


class Animal:
    """Use for Animal parent class."""

    type = 'animal'

    def __init__(self, name):
        """Use when constructing an object and initializing name."""
        self.name = name

    def __str__(self):
        """Use when wanting to print out the parent class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for function to print animal noise."""
        print("Detta djur har vi inget ljud för.")


class Dog(Animal):
    """Use for Dog child class, extending Animal class."""

    type = 'dog'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Dog) noise."""
        print("Voff!")


class Cat(Animal):
    """Use for Cat child class, extending Animal class."""

    type = 'cat'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Cat) noise."""
        print("Mjau!")


class Rooster(Animal):
    """Use for Rooster child class, extending Animal class."""

    type = 'rooster'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    # def make_noise(self):
    #     """Use for (Rooster) noise."""
    #     print('Cock-a-doodle-doo!')


class GoldFish(Animal):
    """Use for GoldFish child class, extending Animal class."""

    type = 'goldfish'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (GoldFish) noise."""
        print("Blubb!")


def sound_off(animal):
    """Use to sound off the animal."""
    animal.make_noise()


def main():
    """Use as main function."""
    print('\nWeek 06, Exercise 01.2, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    # Create Cat child class for c, name = Mewster
    c = Cat('Mewster')
    # Create Dog child class for c, name = Boy
    d = Dog('Boy')
    # Create Rooster child class for r, name = Pecker
    r = Rooster('Pecker')
    # Create GoldFish child class for g, name = Blubber
    g = GoldFish('Blubber')

    print(f'The animal is a {c.type}, named {c.name}, '
          f'it sound like this:')
    sound_off(c)

    press_continue()

    print(f'The animal is a {d.type}, named {d.name}, '
          f'it sound like this:')
    sound_off(d)

    press_continue()

    print(f'The animal is a {r.type}, named {r.name}, '
          f'it sound like this:')
    sound_off(r)

    press_continue()

    print(f'The animal is a {g.type}, named {g.name}, '
          f'it sound like this:')
    sound_off(g)

    press_exit()


if __name__ == "__main__":
    main()
