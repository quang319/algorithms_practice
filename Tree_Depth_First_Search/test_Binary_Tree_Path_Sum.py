from collections import deque
from typing import Deque

import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/RMlGwgpoKKY
Given a binary tree and a number ‘S’, find if the tree has a path from 
root-to-leaf such that the sum of all the node values of that path equals ‘S’.
'''
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def has_path(root: TreeNode, sum):
    if root == None:
        return False
    
    if (root.val == sum) and (not root.left) and (not root.right):
        return True

    new_sum = sum - root.val
    return has_path(root.left, new_sum) or has_path(root.right, new_sum)


class TestSum(unittest.TestCase):

    def createTree(self) -> TreeNode:
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        return root

    def test_case1(self):
        root = self.createTree()
        self.assertEqual(has_path(root, 23), True)
    
    def test_case2(self):
        root = self.createTree()
        self.assertEqual(has_path(root, 16), False)


if __name__ == '__main__':
    unittest.main()