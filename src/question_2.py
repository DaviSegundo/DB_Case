"""
Question 2 presents a problem that demands a slightly deeper level of logical reasoning compared
to Question 1.

The task involves maximizing the value of pairs while ensuring their sum does not surpass a 
predefined threshold. To tackle this, our first step is to sort the list, simplifying the problem.
Once again, we utilize the sorted() method, as explained in the previous question, resulting in an
ordered list by ascending values.

Next, we determine the number of trips required to collect all orders. We accomplish this by 
examining the ends of the sorted list. Two cases arise:

    - Case 1: A feasible pair exists between the highest and lowest values. If their sum remains
    below the maximum threshold, we increment the trip counter by 1, advance the left pointer 
    index by 1, and decrement the right pointer index by 1. This process continues for the 
    remaining elements in the middle of the list.

    - Case 2: The sum of the highest and lowest values exceeds the maximum threshold. In this
    scenario, it's impossible to form a pair within the limit, thus we treat the highest value as
    a single trip. Consequently, we increment the trip counter by 1 and adjust the right pointer 
    index to the next highest value.

This cycle of checks, alternating between Case 1 and Case 2, continues until we determine the total
number of trips needed to collect all orders.

The final computational complexity remains O(n log n), as sorting incurs a cost of  O(n log n), as
specified in the previous question, and traversing the list once using the while loop contributes
O(n).

To evaluate various input scenarios for this problem, refer to the test file for Question 2 
(tests/test_question_2.py), where parameterized test cases are provided.
"""

from typing import List


class Orders:
    """
    Handles the business logic of operations on orders
    """

    def combine_orders(self, requests: List[int], n_max: int) -> int:
        """
        Returns the number of trips necessary to collect all orders, considering that they will be
        grouped two by two and should not exceed the maximum value entered.

        Args:
            requests (List[int]): List of integer values representing the monetary value of orders.
                Ex: [70, 30, 10]
            n_max (int): Maximum value allowed for combining two orders. Ex: 100

        Returns:
            int: The total number of trips to collect all orders
        """
        sorted_list = sorted(requests)
        travel_count = 0

        left_index = 0
        right_index = len(sorted_list) - 1

        while left_index <= right_index:
            if sorted_list[left_index] + sorted_list[right_index] <= n_max:
                left_index += 1
                right_index -= 1
                travel_count += 1
            else:
                right_index -= 1
                travel_count += 1

        return travel_count
