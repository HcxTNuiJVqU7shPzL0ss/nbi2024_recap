"""Module for 'Discuss'.

Lesson 02, Week 06, Exercise 01, parts 2a and 2b.
What does the following code do?
Fix any errors.
TAP HT 25D, though done in near time off course, then
refactored for this week.
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
        print('We do not have a sound for this animal!')


class Dog(Animal):
    """Use for Dog child class, extending Animal class."""

    type = 'dog'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Dog) noise."""
        print('Woof!')


class Cat(Animal):
    """Use for Cat child class, extending Animal class."""

    type = 'cat'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Cat) noise."""
        print('Meow!')


class Rooster(Animal):
    """Use for Rooster child class, extending Animal class."""

    type = 'rooster'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Rooster) noise."""
        print('Cock-a-doodle-doo!')


class GoldFish(Animal):
    """Use for GoldFish child class, extending Animal class."""

    type = 'goldfish'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (GoldFish) noise."""
        print('Blub blub!')


class Parrot(Animal):
    """Use for Parrot child class, extending Animal class."""

    type = 'parrot'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Parrot) noise."""
        print('Polly wants a cracker!')


class GroundHog(Animal):
    """Use for GroundHog child class, extending Animal class."""

    type = 'groundhog'

    def __str__(self):
        """Use when wanting to print out the child class name."""
        return self.__class__.__name__


def sound_off(animal):
    """Use to sound off the animal."""
    animal.make_noise()


def create_animals():
    """Use to create list of animals."""
    build_list = []
    # Create Cat child class for c, name = Mewster
    c = Cat('Mewster')
    build_list.append(c)
    # Create Dog child class for c, name = Boy
    d = Dog('Boy')
    build_list.append(d)
    # Create Rooster child class for r, name = Pecker
    r = Rooster('Pecker')
    build_list.append(r)
    # Create GoldFish child class for g, name = Blubber
    g = GoldFish('Blubber')
    build_list.append(g)
    # Create Parrot child class for p, name = Polly
    p = Parrot('Polly')
    build_list.append(p)
    # Create GroundHog child class for gh, name = Phil
    gh = GroundHog('Phil')
    build_list.append(gh)

    return build_list


def animal_farm(list_of_pets, last_pet):
    """Use to display info of the animal farm."""
    for animal in list_of_pets:
        print(f'The animal is a {animal.type}, named {animal.name}, '
              f'it sounds like this:')
        sound_off(animal)
        if animal != last_pet:
            press_continue()


def main():
    """Use as main function.

    This version made for the recap of 2024.
    Refactored for TAP HT 25D.
    """
    print('\nWeek 06, Exercise 01.2, Discuss.\nFunction: ',
          main.__name__, sep = '')
    press_continue()

    animal_list = create_animals()
    last_one = animal_list[-1]

    animal_farm(animal_list, last_one)

    # print(f'The animal is a {c.type}, named {c.name}, '
    #       f'it sounds like this:')
    # sound_off(c)
    # press_continue()
    #
    # print(f'The animal is a {d.type}, named {d.name}, '
    #       f'it sounds like this:')
    # sound_off(d)
    # press_continue()
    #
    # print(f'The animal is a {r.type}, named {r.name}, '
    #       f'it sounds like this:')
    # sound_off(r)
    # press_continue()
    #
    # print(f'The animal is a {g.type}, named {g.name}, '
    #       f'it sounds like this:')
    # sound_off(g)
    # press_continue()
    #
    # print(f'The animal is a {p.type}, named {p.name}, '
    #       f'it sounds like this:')
    # sound_off(p)
    # press_continue()
    #
    # print(f'The animal is a {gh.type}, named {gh.name}, '
    #       f'it sounds like this:')
    # sound_off(gh)

    press_exit()


if __name__ == "__main__":
    main()
