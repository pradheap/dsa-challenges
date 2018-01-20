import unittest

from lib.source.graph import WeightedGraph, UnweightedGraph
from challenges.graph.source.traversal import *

class TestTraversal(unittest.TestCase): 
    def test_recursive_dfs(self):
        graph = WeightedGraph(is_directed=False)
        graph.add_edge('a', 'b')
        graph.add_edge('a', 'c')
        graph.add_edge('b', 'd')
        graph.add_edge('b', 'b1')
        graph.add_edge('d', 'e')
        self.assertEqual(recursive_dfs(graph, 'a'), ['a', 'b', 'd', 'e', 'b1', 'c'])
    
    def test_iterative_dfs(self):
        graph = WeightedGraph(is_directed=False)
        graph.add_edge('a', 'b')
        graph.add_edge('a', 'c')
        graph.add_edge('b', 'd')
        graph.add_edge('b', 'b1')
        graph.add_edge('d', 'e')
        self.assertEqual(iterative_dfs(graph, 'a'), ['a', 'c', 'b', 'b1', 'd', 'e'])
    
    def test_iterative_bfs(self):
        graph = WeightedGraph(is_directed=False)
        graph.add_edge('a', 'b')
        graph.add_edge('a', 'c')
        graph.add_edge('b', 'd')
        graph.add_edge('b', 'b1')
        graph.add_edge('d', 'e')
        self.assertEqual(iterative_bfs(graph, 'a'), ['a', 'b', 'c', 'd', 'b1', 'e'])