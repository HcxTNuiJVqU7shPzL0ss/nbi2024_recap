"""Module for this exercise.

Use for exercise 1, parts 2a and b.
"""


class Animal:
    """Use for Animal class."""

    type = 'animal'

    def __init__(self, name):
        """Use for name."""
        self.name = name

    def __str__(self):
        """Use for str."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for function."""
        print("Detta djur har vi inget ljud för.")


class Dog(Animal):
    """Use for Dog."""

    type = 'dog'

    def __str__(self):
        """Use for str."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Dog)."""
        print("Voff!")


class Cat(Animal):
    """Use for Cat."""

    type = 'cat'

    def __str__(self):
        """Use for str."""
        return self.__class__.__name__

    def make_noise(self):
        """Use for (Cat)."""
        print("Mjau!")


class Rooster(Animal):
    """Use for Rooster."""

    def __str__(self):
        """Use for str."""
        return self.__class__.__name__

    # def make_noise(self):
    #     """Use for make_noise (Rooster)."""
    #     print('Cock-a-doodle-doo!')


def sound_off(animal):
    """Use to sound off the animal."""
    animal.make_noise()



def main():
    """Use as main function."""
    print('\nWeek 05, Exercise 01.1, Discuss.\nFunction: ',
          main.__name__, sep = '')
    c = Cat('Mewster')
    d = Dog('Boy')
    h = Rooster('Pecker')
    sound_off(c)
    sound_off(d)
    sound_off(h)
    print(Dog.type)
    print(Rooster.type)


if __name__ == "__main__":
    main()
