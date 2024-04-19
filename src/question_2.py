"""
For question 2 we have a problem that requires a little more logical reasoning compared to
question 1.

Here we have the idea of making combinations of pairs that maximize the value without exceeding the
established threshold of the value that the sum of the two elements of the group can have.

Therefore, what we need to do first is sort the list to simplify the problem, which is where the 
`sorted()` method comes in again, which was already explained in the previous question. With this,
we have a list ordered by the values in ascending order.

Therefore, it remains to calculate how many trips will be necessary to collect all the orders, 
which will be done by checking the ends of the list, where it will be analyzed whether it is 
possible to combine the highest value order with the lowest value or not. Thus, we have: 
    
    - Case 1: which constitutes a possible pair between the largest and the smallest, if their sum
    does not exceed the maximum value allowed and 1 is added to the travel counter and the left 
    pointer index increases by 1 and the index of the right pointer is reduced by 1, so we increase
    the trip counter by 1, causing the check to continue for the remaining elements in the middle 
    of the list. 
    
    - Case 2: where the largest value added to the smallest exceeds the maximum allowed value, 
    which we can conclude that it is impossible for there to be a value that, combined with it, 
    does not exceed the allowed limit, so we can reach the conclusion that it must be considered 
    as a single trip, so we increase the trip counter by 1 and reduce the right pointer index to 
    go to the new highest value.

And so the checks continue varying between case 1 and 2 until we reach the total number of trips 
needed to collect all orders.

With this we have a final complexity of O(n log n), as our sorting cost was O(n log n), as already
specified in the previous question and we have the cost O(n) to go through the list once using the
while loop.

The tests for the possible input cases of this problem can be found in the test file for question 2
(tests/test_question_2.py), where cases are parameterized as test input.
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
