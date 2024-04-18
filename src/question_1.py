"""

"""  # TODO: Add thoughts on question 1

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
