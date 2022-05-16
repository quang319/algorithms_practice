from collections import deque

import unittest

'''
https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00

Topological Sort of a directed graph (a graph with unidirectional edges) is a 
linear ordering of its vertices such that for every directed edge (U, V) 
from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.
'''
def topological_sort(vertices, edges):
    if vertices <= 0:
        return []
    sorted_result = []

    # a) Init the graph
    in_edges = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # b) building the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_edges[child] += 1

    # c) find the sources
    sources = deque()
    for key in in_edges:
        if in_edges[key] == 0:
            sources.append(key)
    
    # d)
    while sources:
        vertex = sources.popleft()
        sorted_result.append(vertex)

        for child in graph[vertex]:
            in_edges[child] -= 1
            if in_edges[child] == 0:
                sources.append(child)
    
    if len(sorted_result) != vertices:
        return []
    return sorted_result

class TestSum(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]), [3, 2, 0, 1])

    def test_case2(self):
        self.assertEqual(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]), [4, 2, 3, 0, 1])

    def test_case3(self):
        self.assertEqual(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]), [5, 6, 3, 4, 0, 2, 1])


if __name__ == '__main__':
    unittest.main()