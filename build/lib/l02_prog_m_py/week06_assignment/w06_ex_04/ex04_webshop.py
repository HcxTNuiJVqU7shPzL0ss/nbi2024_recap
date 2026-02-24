"""Module for 'Webshop'.

Lesson 02, Week 06, Exercise 04.
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


class Product:
    """Use as class to handle various products."""

    def __init__(self, id_p:int, name:str, price:float):
        """Use when constructing and initializing an object."""
        self.__id_p = id_p
        self.__name = name
        self.__price = price

    def __str__(self):
        """Use to create human-readable output."""
        return (f'Product information: ID {self.__id_p}, '
                f'Name {self.__name}, Price {self.__price}')

    @property
    def idp(self):
        """Use to return ID."""
        return self.__id_p

    @property
    def name(self):
        """Use to return name."""
        return self.__name

    @property
    def price(self):
        """Use to return price."""
        return self.__price


class Order:
    """Use as class to handle when an order is made."""

    def __init__(self, id_o:int, order:list):
        """Use when constructing and initializing an object."""
        self.__id_o = id_o
        self.__order = order

        total_cost = 0
        for i in self.__order:
            item = i[0]
            item_pcs = i[1]
            total_cost += item.price * item_pcs
        self.__total_cost = total_cost

    def __str__(self):
        """Use to create human-readable output."""
        return f'Order: ID {self.__id_o}'

    @property
    def ido(self):
        """Use to return ID."""
        return self.__id_o

    @property
    def order(self):
        """Use to return the order."""
        return self.__order

    @property
    def total_cost(self):
        """Use to return the total cost of the order."""
        return self.__total_cost


class ShoppingCart:
    """Use as class to handle a shoppingcart."""

    def __init__(self, id_s:int):
        """Use when constructing and initializing an object."""
        self.__id_s = id_s
        self.__cart = []

    def __str__(self):
        """Use to create human-readable output."""
        return f'Shoppingcart: ID {self.__id_s}'

    @property
    def ids(self):
        """Use to return ID."""
        return self.__id_s

    @property
    def cart(self):
        """Use to return the cart."""
        return self.__cart

    @property
    def total_cost(self):
        """Use to return the total cost of the order."""
        total_cost = 0
        for i in self.__cart:
            item = i[0]
            item_pcs = i[1]
            total_cost += item.price * item_pcs
        return total_cost

    def add_to_cart(self, item:Product, item_pcs:int):
        """Use to add an item to the cart."""
        self.__cart.append([item, item_pcs])


def go_shopping():
    """Use to add products, add to shoppingcart and place order."""
    # Products available
    hammer_drill = Product(1, 'Hammer Drill 750W', 899)
    cordless_drill = Product(2, 'Cordless Drill 18V', 1299)
    circular_saw = Product(3, 'Circular Saw 1600W', 1499)
    multi_tool = Product(4, 'Multi‑Tool 300W', 749)
    laser_distance_meter = Product(5, 'Laser Distance Meter', 999)
    toolbox = Product(6, 'Toolbox 50cm', 399)
    hammer_proline = Product(7, 'Hammer ProLine', 199)
    bit_set_32_pcs = Product(8, 'Bit Set 32 Pieces', 149)
    led_work_light = Product(9, 'LED Work Light', 349)
    spirit_level = Product(10, 'Spirit Level 60cm', 129)
    # Create a shoppingcart
    shopping_cart_1 = ShoppingCart(1001)
    shopping_cart_1.add_to_cart(hammer_drill, 11)
    shopping_cart_1.add_to_cart(cordless_drill, 12)
    shopping_cart_1.add_to_cart(circular_saw, 13)
    shopping_cart_1.add_to_cart(multi_tool, 14)
    shopping_cart_1.add_to_cart(laser_distance_meter, 15)
    shopping_cart_1.add_to_cart(toolbox, 16)
    shopping_cart_1.add_to_cart(hammer_proline, 17)
    shopping_cart_1.add_to_cart(bit_set_32_pcs, 18)
    shopping_cart_1.add_to_cart(led_work_light, 19)
    shopping_cart_1.add_to_cart(spirit_level, 101)
    # for item in shopping_cart_1.cart:
    #     print(item[0], item[1])
    # Place an order
    order_1 = Order(2001, shopping_cart_1.cart)
    to_pay = order_1.total_cost
    print(f'In total, your order will cost {to_pay} SEK')


def main():
    """Use as module for Main.

    TAP HT 25D, though done in near time off course, then
    refactored for this week.
    """
    print('\nLesson 02, Week 06, Exercise 04, Webshop.')
    press_continue()

    go_shopping()

    press_exit()


if __name__ == "__main__":
    main()
