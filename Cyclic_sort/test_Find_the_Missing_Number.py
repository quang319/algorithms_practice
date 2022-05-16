import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/JPnp17NYXE9
We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.
'''
def find_missing_number(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        if (nums[i] < n) and (nums[i] != nums[j]):
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if i != nums[i]:
            return i

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(find_missing_number([4, 0, 3, 1]), 2)

    def test_case2(self):
        self.assertEqual(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]), 7)


if __name__ == '__main__':
    unittest.main()