from cProfile import run
from collections import deque
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
            
def has_cycle(head : Node):
    slow, fast = head, head

    while (fast != None) and (fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False

    
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

class TestSum(unittest.TestCase):

    def createNode(self) -> Node:
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        return head

    def test_case1(self):
        head = self.createNode()
        self.assertEqual(has_cycle(head), False)

    def test_case2(self):
        head = self.createNode()
        head.next.next.next.next.next.next = head.next.next
        self.assertEqual(has_cycle(head), True)

    def test_case2(self):
        head = self.createNode()
        head.next.next.next.next.next.next = head.next.next.next
        self.assertEqual(has_cycle(head), True)


if __name__ == '__main__':
    unittest.main()