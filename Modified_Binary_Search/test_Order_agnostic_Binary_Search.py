
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/R8LzZQlj8lO
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. 
You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
'''
def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] < arr[end]

    while start <= end: 
        mid = start + ((end - start) // 2)
        mid_val = arr[mid]

        if mid_val == key:
            return mid

        if is_ascending:
            if key < mid_val:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < mid_val:
                start = mid + 1
            else:
                end = mid - 1
    return -1

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(binary_search([4, 6, 10], 10), 2)

    def test_case2(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 5), 4)

    def test_case3(self):
        self.assertEqual(binary_search([10, 6, 4], 10), 0)

    def test_case4(self):
        self.assertEqual(binary_search([10, 6, 4], 4), 2)


if __name__ == '__main__':
    unittest.main()