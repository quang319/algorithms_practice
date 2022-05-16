from ast import Interactive
from threading import currentThread
from typing import List
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/3jyVPKRA8yx
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
'''
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Interval):
            return (self.start == other.start) and (self.end == other.end) 
        return False
    def __str__ (self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"
    
    def to_list (self):
        return [self.start, self.end]

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')
        
def merge(intervals: List[Interval]):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start, end = intervals[0].start, intervals[0].end
    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        
        is_overlapped = current_interval.start <= end
        if is_overlapped:
            end = max(end, current_interval.end)
        else:
            # not overlapped
            merged_intervals.append(Interval(start, end))
            start = current_interval.start
            end = current_interval.end

    merged_intervals.append(Interval(start, end))

    return merged_intervals
            




class TestSum(unittest.TestCase):

    def test_case1(self):
        result = merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)])
        self.assertEqual([x.to_list() for x in result], [[1, 5], [7, 9]])

    def test_case2(self):
        result = merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)])
        self.assertEqual([x.to_list() for x in result], [[2, 4], [5, 9]])

    def test_case3(self):
        result = merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)])
        self.assertEqual([x.to_list() for x in result], [[1, 6]])


if __name__ == '__main__':
    unittest.main()