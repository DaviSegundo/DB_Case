# pylint: disable=missing-function-docstring
"""
Module that contains tests related to question 1, where different types of input that the method 
could have were validated.
"""

from src.question_1 import Contract
from src.question_1 import Contracts


def test_get_top_n_base_case():
    contracts_list = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5),
    ]
    renegotiated_contracts = [3]
    top_n = 3

    contracts_handler = Contracts()
    actual_open_contracts = contracts_handler.get_top_n_open_contracts(
        open_contracts=contracts_list, renegotiated_contracts=renegotiated_contracts, top_n=top_n
    )

    expected_open_contracts = [5, 4, 2]
    assert actual_open_contracts == expected_open_contracts


def test_get_top_n_empty_list():
    contracts_list = []
    renegotiated_contracts = [3]
    top_n = 3

    contracts_handler = Contracts()
    actual_open_contracts = contracts_handler.get_top_n_open_contracts(
        open_contracts=contracts_list, renegotiated_contracts=renegotiated_contracts, top_n=top_n
    )

    expected_open_contracts = []
    assert actual_open_contracts == expected_open_contracts


def test_get_top_n_all_contracts_renegotiated():
    contracts_list = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5),
    ]
    renegotiated_contracts = [1, 2, 3, 4, 5]
    top_n = 3

    contracts_handler = Contracts()
    actual_open_contracts = contracts_handler.get_top_n_open_contracts(
        open_contracts=contracts_list, renegotiated_contracts=renegotiated_contracts, top_n=top_n
    )

    expected_open_contracts = []
    assert actual_open_contracts == expected_open_contracts


def test_get_top_n_no_contracts_renegotiated():
    contracts_list = [
        Contract(id=1, debt=5000),
        Contract(id=2, debt=2500),
        Contract(id=3, debt=3200),
        Contract(id=4, debt=800),
        Contract(id=5, debt=4500),
    ]
    renegotiated_contracts = []
    top_n = 4

    contracts_handler = Contracts()
    actual_open_contracts = contracts_handler.get_top_n_open_contracts(
        open_contracts=contracts_list, renegotiated_contracts=renegotiated_contracts, top_n=top_n
    )

    expected_open_contracts = [1, 5, 3, 2]
    assert actual_open_contracts == expected_open_contracts


def test_get_top_n_with_n_higher_than_len_of_contracts_list():
    contracts_list = [
        Contract(id=1, debt=5000),
        Contract(id=2, debt=2500),
        Contract(id=3, debt=3200),
        Contract(id=4, debt=800),
        Contract(id=5, debt=4500),
    ]
    renegotiated_contracts = []
    top_n = 7

    contracts_handler = Contracts()
    actual_open_contracts = contracts_handler.get_top_n_open_contracts(
        open_contracts=contracts_list, renegotiated_contracts=renegotiated_contracts, top_n=top_n
    )

    expected_open_contracts = [1, 5, 3, 2, 4]
    assert actual_open_contracts == expected_open_contracts
