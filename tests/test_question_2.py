# pylint: disable=missing-function-docstring
"""
Module that contains tests related to question 2, where different types of input that the method 
could have were validated.
"""

from typing import List

import pytest

from src.question_2 import Orders


@pytest.mark.parametrize(
    argnames=["requests_list", "n_max", "expected_travels"],
    argvalues=(
        ([70, 30, 10], 100, 2),  # Base Case
        ([70, 30, 10, 95], 100, 3),  # New order that cannot be joined
        ([70, 30, 10, 90], 100, 2),  # New Order that can be joined
        ([91, 92, 93, 94, 95], 100, 5),  # Only one travels
        ([], 100, 0),  # No travels
        ([50], 100, 1),  # One travel
        ([90, 20, 100, 10, 110, 95, 5, 40, 50], 110, 5),  # Case more realistic 1
        ([90, 20, 100, 10, 110, 95, 5, 40, 50, 30], 110, 6),  # Case more realistic 2
        ([20, 20, 20, 20, 20], 80, 3),  # Case with same numbers
    ),
)
def test_combine_orders(requests_list: List[int], n_max: int, expected_travels: int):
    orders_handler = Orders()
    travels_count = orders_handler.combine_orders(requests=requests_list, n_max=n_max)

    assert travels_count == expected_travels
