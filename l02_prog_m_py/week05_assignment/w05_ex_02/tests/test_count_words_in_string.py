"""Module for tests, L02, W05, Ex02.

Part 2.2 function test.
This one here can be considered extensive and very
overworked, used for learning things.
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


import pytest


from ..src.count_words_in_string import count_words_in_sentence


###


### Special Exception Type ###
@pytest.mark.parametrize(
    'sentence_in',
    [
        273,
        42.42,
        [3.14],
        (23, 31),
        {'yes': 42},
        {14, 42, 41},
        range(42),
        b'bcdef',
        bytearray(b'bcdef'),
        None,
        True,
        False,
        lambda y: y,
        (i for i in range(3)),
        iter([1, 2, 3, 4]),
    ],
)

def test_count_words_in_sentence__wrong_types_raise_typeerror(sentence_in):
    """Use for TypeError raise testing.

    Tests req_001, including ac_001.
    However, instead of returning False, will raise TypeError.
    """
    with pytest.raises(TypeError):
        count_words_in_sentence(sentence_in)


###


### Special Exception Value: Empty string ###
@pytest.mark.parametrize(
    'sentence_in',
    [
        '',
        "",
    ],
)

def test_count_words_in_sentence__empty_string(sentence_in):
    """Use for ValueError raise testing, empty string.

    Tests:
    req_002, including ac_002
    req_004 and ac_004 (bullet 2)
    However, instead of returning None, will raise ValueError.
    """
    with pytest.raises(ValueError):
        count_words_in_sentence(sentence_in)


###


### Special one ###
@pytest.mark.parametrize(
    'sentence_in',
    [
        'a',
        ' one',
        '1 ',
        ' b ',
        '     c   ',
        '    all_is_just_one_word   '
    ],
)

def test_count_words_in_sentence__count_one_word(sentence_in):
    """Use for check of counting one word.

    Part of checking:
    req_003 and ac_003
    req_004 and ac_004
    req_005 and ac_005
    """
    assert count_words_in_sentence(sentence_in) == 1


###


### Special two ###
@pytest.mark.parametrize(
    'sentence_in',
    [
        'a b',
        ' one two',
        '1 2 ',
        ' c d ',
        '  e   f   ',
        'now_we_use   two_words',
    ],
)

def test_count_words_in_sentence__count_two_words(sentence_in):
    """Use for check of counting two words.

    Part of checking:
    req_003 and ac_003
    req_004 and ac_004
    req_005 and ac_005
    """
    assert count_words_in_sentence(sentence_in) == 2
