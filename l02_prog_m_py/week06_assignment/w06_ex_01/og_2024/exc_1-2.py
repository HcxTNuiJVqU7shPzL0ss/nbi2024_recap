# pylint: skip-file
# noqa


class Animal:
    # noqa
    def make_noise(self):
        # noqa
        print("Detta djur har vi inget ljud för.")


class Dog(Animal):
    # noqa
    def make_noise(self):
        # noqa
        print("Voff!")

class Cat(Animal):
    # noqa
    def make_noise(self):
        # noqa
        # super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    # noqa
    def make_noise(self):
        # noqa
        print("Cock-a-doodle-do!")

class Goldfish(Animal):
    # noqa
    def make_noise(self):
        # noqa
        super().make_noise()


def sound_off(animal):
    # noqa
    animal.make_noise()


c = Cat()
d = Dog()
h = Rooster()
gf = Goldfish()

animals = [c, d, h, gf]

for animal in animals:
    sound_off(animal)

# sound_off(c)
# sound_off(d)
# sound_off(h)
# sound_off(gf)
