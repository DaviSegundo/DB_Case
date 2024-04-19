"""
For Question 1, we encounter a challenge that revolves around two primary aspects: filtering and 
sorting.

Given the expectation of a considerable number of renegotiated contracts, likely leading to a 
substantial reduction in the dataset for subsequent ordering operations, our approach begins with
a straightforward filtering step. This initial pass through the list serves to eliminate 
identifiers associated with contracts that have already undergone renegotiation. This filtering 
process incurs a computational cost of O(n), where n represents the size of the dataset.

Following the filtering phase, the next step involves sorting the remaining contracts based on the
value of open contracts that haven't undergone renegotiation. To accomplish this, we leverage 
Python's built-in sorted() method, which employs the Timsort algorithm. With an average and 
worst-case time complexity of O(n log n), Timsort stands as an efficient choice, particularly for
handling large datasets.

With the dataset now filtered and sorted, we simply need to extract the top N values and return
them as a list containing only the identifiers. This approach yields a final computational 
complexity of O(n log n).

The test suite for evaluating various input scenarios related to this problem can be found in the
designated test file for Question 1 (tests/test_question_1.py). Each test case within the file is
labeled to indicate the specific validation it aims to perform.
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
