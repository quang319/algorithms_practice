import numbers
from typing import List
from heapq import *
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/RM535yM9DW0

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
'''

def find_k_largest_numbers(nums, k):
    min_heap = []

    for i in range(k):
        heappush(min_heap, nums[i])
    
    for i in range(k, len(nums)):
        current_val = nums[i]
        if current_val > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, current_val)
    return min_heap

class TestSum(unittest.TestCase):

    def test_case1(self):
        arr = [1, 4, 2, 1, 3, 2, 3]
        self.assertEqual(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3), [5, 12, 11])
    
    def test_case2(self):
        arr = [1, 4, 2, 1, 3, 2, 3]
        self.assertEqual(find_k_largest_numbers([5, 12, 11, -1, 12], 3), [11, 12, 12])


if __name__ == '__main__':
    unittest.main()