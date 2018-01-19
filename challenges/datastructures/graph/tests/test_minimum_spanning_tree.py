import unittest

from lib.source.graph import WeightedGraph
from challenges.datastructures.graph.source.minimum_spanning_tree import *

class TestMinimumSpanningTree(unittest.TestCase):
    def test_minimum_spanning_tree(self):
        graph = WeightedGraph()
        graph.add_edge('a', 'b', 6)
        graph.add_edge('b', 'c', 7)
        graph.add_edge('c', 'd', 8)
        graph.add_edge('d', 'e', 9)
        graph.add_edge('e', 'f', 10)
        graph.add_edge('f', 'a', 5)
        graph.add_edge('b', 'f', 11)
        graph.add_edge('e', 'b', 12)
        graph.add_edge('c', 'e', 13)
        self.assertEqual(minimum_spanning_tree(graph), 35)
    
    def test_minimum_spanning_tree_v1(self):
        graph = WeightedGraph()
        graph.add_edge('a', 'b', 10)
        graph.add_edge('a', 'c', 15)
        graph.add_edge('c', 'e', 20)
        graph.add_edge('e', 'f', 15)
        graph.add_edge('f', 'd', 25)
        graph.add_edge('b', 'd', 10)
        graph.add_edge('b', 'c', 5)
        graph.add_edge('f', 'c', 5)
        graph.add_edge('c', 'd', 5)
        self.assertEqual(minimum_spanning_tree(graph), 40)
