"""
For question 1 we have a problem that involves two main points, filtering and ordering.

Considering that it is possible to expect a number of renegotiated contracts that will 
significantly reduce the data set on which the ordering will be carried out, we have to apply a 
simple filter that first goes through the list once and removes the identifiers of contracts 
that have already been renegotiated, which will have a computational cost of O(n).

After the filtering process, we will perform the ordering, based on the value of open contracts
that have not been renegotiated. For this, the built-in python `sorted()` method was used, which 
uses the Timsort algorithm, which has a complexity of O(n log n) in the average case and in the
worst case, making it an efficient choice for large sets of data.

This way, with the data filtered and ordered, we just need to take the top_n values and return
them in a list with only the identifiers to obtain the solution to the proposed problem, which 
results in a final complexity of O(n log n).

The tests for the possible input cases of this problem can be found in the test file for question 1
(tests/test_question_1.py), there the nomenclature of the tests represents what they are proposing 
to be validated.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Contract:
    """
    Representation of a customer's contract data

    Args:
        id (int): Customer identifier. Ex: 88
        debt (float):  Total amount of customer debts Ex: 7542.98
    """

    id: int
    debt: float

    def __str__(self) -> str:
        return f"id={self.id}, debt={self.debt}"


class Contracts:
    """
    Handles the business logic of operations on contracts
    """

    def get_top_n_open_contracts(
        self, open_contracts: List[Contract], renegotiated_contracts: List[int], top_n: int
    ) -> List[int]:
        """
        Returns the N largest debtors IDs who have not yet had their debts renegotiated.

        Args:
            open_contracts (List[Contract]): List of open contracts.
                Ex: [Contract(id=1, debt=5000),Contract(id=2, debt=2500),...]
            renegotiated_contracts (List[int]): List of IDs of customers whose contracts have
                already been renegotiated and must be filtered. Ex: [3, 4]
            top_n (int): Number of the N largest debtors that must be returned. Ex: 2

        Returns:
            List[int]: List with the IDs of the largest debtors with open and non-renegotiated
                contracts.
        """
        open_contracts_filter_list = [
            contract for contract in open_contracts if contract.id not in renegotiated_contracts
        ]
        open_contracts_sorted_list = sorted(
            open_contracts_filter_list, key=lambda contract: contract.debt, reverse=True
        )

        top_n_open_contracts_list = open_contracts_sorted_list[:top_n]
        top_n_id_list = [contract.id for contract in top_n_open_contracts_list]

        return top_n_id_list
