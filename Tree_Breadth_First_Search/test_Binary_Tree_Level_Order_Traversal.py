from asyncio import QueueEmpty
from collections import deque
from typing import Deque

import unittest
from unittest import result

'''
https://www.educative.io/courses/grokking-the-coding-interview/xV7E64m4lnz
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root: TreeNode):
    if not root:
        return []
    
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        current_level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            parent = queue.popleft()
            current_level.append(parent.val)

            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)
        
        result.append(current_level)
    return result
            


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
        self.assertEqual(traverse(root), [[12], [7, 1], [9, 10, 5]])


if __name__ == '__main__':
    unittest.main()