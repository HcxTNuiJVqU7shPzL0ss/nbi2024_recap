"""Module for tests, L02, W04, Ex04.

Handle unit test of function: create_and_return_card
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


# pylint: disable=import-error
from ..ex04_functions import create_and_return_card
# pylint: enable=import-error


def test_create_and_return_card__correct_values():
    """Use for unit test of function create_and_return_card.

    Checks that the returned value contains suit and rank
    which lies within what is expected.
    """
    list_of_cards = []
    accepted_suits = ['spades', 'clubs', 'hearts', 'diamonds']
    accepted_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    cnt_cards = 0
    # Should be able to run this 52 times
    while cnt_cards < 52:
        deal_card = create_and_return_card(list_of_cards)
        list_of_cards.append(deal_card)
        card_suit = deal_card[0]
        card_rank = deal_card[1]
        assert card_suit in accepted_suits
        assert card_rank in accepted_ranks
        cnt_cards += 1
    assert cnt_cards == 52


def test_create_and_return_card__not_list():
    """Used for unit test of function create_and_return_card.

    Check that sending in different argument than
    list to parameter for what to find returns None.
    """
    use_int_not_list_create = 42
    use_float_not_list_create = 42.42
    use_str_not_list_create = '42'
    use_tuple_not_list_create = ('42', '42')
    check_list_of_wrong_create = [use_int_not_list_create,
                              use_float_not_list_create,
                              use_str_not_list_create,
                              use_tuple_not_list_create]
    for check_list_create in check_list_of_wrong_create:
        assert create_and_return_card(check_list_create) is None
