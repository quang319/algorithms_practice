from heapq import *
from typing import List
import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/Y5n0n3vAgYK
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
'''
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value



def merge_lists(lists: List[ListNode]):
    min_heap = []

    for node in lists:
        heappush(min_heap, node)
    
    current_head, current_tail = None, None
    while len(min_heap) > 0:
        node = heappop(min_heap)

        if not current_head:
            current_head = current_tail = node
        else:
            current_tail.next = node
            current_tail = current_tail.next
        
        if node.next:
            heappush(min_heap, node.next)
    return current_head
        


class TestSum(unittest.TestCase):

    def test_case1(self):
        l1 = ListNode(2)
        l1.next = ListNode(6)
        l1.next.next = ListNode(8)

        l2 = ListNode(3)
        l2.next = ListNode(6)
        l2.next.next = ListNode(7)

        l3 = ListNode(1)
        l3.next = ListNode(3)
        l3.next.next = ListNode(4)
        result: ListNode = merge_lists([l1, l2, l3])
        result_list = []
        while result != None:
            result_list.append(result.value)
            result = result.next
            
        self.assertEqual(result_list, [1, 2, 3, 3, 4, 6, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()