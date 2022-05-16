from cProfile import run
from collections import deque
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
'''
def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1

    current_sum = 0
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if target_sum == current_sum:
            return [left, right]
        
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return [-1, -1]


class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(pair_with_targetsum([1, 2, 3, 4, 6], 6), [1, 3])

    def test_sum_tuple(self):
        self.assertEqual(pair_with_targetsum([2, 5, 9, 11], 11), [0, 2])


if __name__ == '__main__':
    unittest.main()