from cProfile import run
from collections import deque
import numbers
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/gx2OqlvEnWG
Given a set with distinct elements, find all of its distinct subsets.
'''
def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            cur_subset = list(subsets[i])
            cur_subset.append(num)
            subsets.append(cur_subset)
    return subsets

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(find_subsets([1, 3]), [[], [1], [3], [1, 3]])

    def test_case2(self):
        self.assertEqual(find_subsets([1, 5, 3]), [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]])


if __name__ == '__main__':
    unittest.main()