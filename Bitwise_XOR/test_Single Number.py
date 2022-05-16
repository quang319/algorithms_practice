import numbers
from typing import List
from heapq import *
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/gk20xz4VwpG

In a non-empty array of integers, every number appears twice except for one, find that single number.
'''

def find_single_number(arr):
    xored = 0
    for num in arr:
        xored ^= num
    return xored    

class TestSum(unittest.TestCase):

    def test_case1(self):
        arr = [1, 4, 2, 1, 3, 2, 3]
        self.assertEqual(find_single_number(arr), 4)


if __name__ == '__main__':
    unittest.main()