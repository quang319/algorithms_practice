import numbers
from typing import List
from heapq import *
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/3Yj2BmpyEy4

Design a class to calculate the median of a number stream. The class should have the following two methods:

    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
'''

class MedianOfAStream:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert_num(self, num):
        if (not self.max_heap) or (-self.max_heap[0] >= num):
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        if len(self.max_heap) > (len(self.min_heap) + 1):
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] / 2.0) + (self.min_heap[0] / 2.0)
        
        return -self.max_heap[0] / 1.0
        

class TestSum(unittest.TestCase):

    def test_case1(self):
        medianOfAStream = MedianOfAStream()
        medianOfAStream.insert_num(3)
        medianOfAStream.insert_num(1)
        self.assertEqual(medianOfAStream.find_median(), 2.0)

    def test_case2(self):
        medianOfAStream = MedianOfAStream()
        medianOfAStream.insert_num(3)
        medianOfAStream.insert_num(1)
        medianOfAStream.insert_num(5)
        self.assertEqual(medianOfAStream.find_median(), 3.0)
    
    def test_case3(self):
        medianOfAStream3 = MedianOfAStream()
        medianOfAStream3.insert_num(3)
        medianOfAStream3.insert_num(1)
        medianOfAStream3.insert_num(5)
        medianOfAStream3.insert_num(4)
        self.assertEqual(medianOfAStream3.find_median(), 3.5)


if __name__ == '__main__':
    unittest.main()