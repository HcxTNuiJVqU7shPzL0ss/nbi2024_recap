"""Module for tests, L02, W04, Ex03, version 3.

Check pulled card.
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
from ..ex03_functions import ex03_v3_pull_card
# pylint: enable=import-error


def test_ex03_v3_pull_card__check_card():
    """Use for unit test of function ex03_v3_pull_card.

    Will check that the returned card is between 1 and 13.
    """
    dealt_card = ex03_v3_pull_card()
    assert 1 <= dealt_card <= 13
