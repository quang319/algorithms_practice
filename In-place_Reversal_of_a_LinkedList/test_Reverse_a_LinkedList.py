from cProfile import run
from collections import deque
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/3wENz1N4WW9
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def as_list(self):
        ret = []
        temp = self
        while temp is not None:
            ret.append(temp.value)
            temp = temp.next
        return ret

def reverse(head: Node):
    if not head:
        return head
    
    previous, current, next = None, head, None
    while current != None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


class TestSum(unittest.TestCase):

    def createNode(self) -> Node:
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)
        return head

    def test_case1(self):
        head = self.createNode()
        self.assertEqual(reverse(head).as_list(), [10, 8, 6, 4, 2])


if __name__ == '__main__':
    unittest.main()