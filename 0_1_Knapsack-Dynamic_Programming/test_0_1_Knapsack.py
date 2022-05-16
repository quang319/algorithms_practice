
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/gkZNLjV2kBk

Given the weights and profits of ‘N’ items, we are asked to put these items in a 
knapsack with a capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. 
Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack 
to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, 
such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit, 
and the total weight does not exceed the capacity.
'''
def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, current_index):
    # base case
    if (capacity <= 0) or (current_index >= len(profits)):
        return 0

    # check if we have already solve the problem
    if dp[current_index][capacity] != -1:
        return dp[current_index][capacity]
    
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + \
            knapsack_recursive(dp, profits, weights, capacity - weights[current_index], current_index+1)
    
    profit2 = knapsack_recursive(dp, profits, weights, capacity, current_index+1)

    dp[current_index][capacity] = max(profit1, profit2)
    return dp[current_index][capacity]

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7), 22)

    def test_case2(self):
        self.assertEqual(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6), 17)

if __name__ == '__main__':
    unittest.main()