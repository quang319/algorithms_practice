from cProfile import run
from collections import deque
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
'''
def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        # check if the window has been completely filled up
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]), 9, "Should be 9")

    def test_case2(self):
        self.assertEqual(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()