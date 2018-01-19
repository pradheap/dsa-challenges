import unittest

from lib.source.graph import *

class TestGraph(unittest.TestCase):
    def test_vertex(self):
        vertex = Vertex('a')
        self.assertEqual(vertex.get_neighbors(), [])
        vertex.add_neighbor('b')
        self.assertEqual(vertex.get_neighbors(), ['b'])
        self.assertEqual(vertex.get_weight('b'), 0)
        vertex.add_neighbor('c', 10)
        self.assertEqual(vertex.get_neighbors(), ['b', 'c'])
        self.assertEqual(vertex.get_weight('c'), 10)
        vertex.remove_neighbor('c')
        self.assertEqual(vertex.get_neighbors(), ['b'])

    def test_undirected_unweighted_graph(self):
        uw_graph = UnweightedGraph()
        uw_graph.add_vertex('a')
        uw_graph.add_vertex('b')
        uw_graph.add_vertex('c')
        uw_graph.add_vertex('d')
        self.assertFalse(uw_graph.is_directed())
        self.assertEqual(uw_graph.get_vertices(), ['a', 'b', 'c', 'd'])
        uw_graph.add_edge('a', 'b')
        uw_graph.add_edge('a', 'c')
        uw_graph.add_edge('b', 'c')
        self.assertEqual(uw_graph.get_edges(), 
        [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')])
        self.assertEqual(uw_graph.get_neighbors('a'), ['b', 'c'])
        self.assertEqual(uw_graph.get_neighbors('b'), ['a', 'c'])
    
    def test_directed_unweighted_graph(self):
        uw_graph = UnweightedGraph(is_directed=True)
        uw_graph.add_vertex('a')
        uw_graph.add_vertex('b')
        uw_graph.add_vertex('c')
        uw_graph.add_vertex('d')
        self.assertTrue(uw_graph.is_directed())
        self.assertEqual(uw_graph.get_vertices(), ['a', 'b', 'c', 'd'])
        uw_graph.add_edge('a', 'b')
        uw_graph.add_edge('a', 'c')
        uw_graph.add_edge('b', 'c')
        self.assertEqual(uw_graph.get_edges(), 
        [('a', 'b'), ('a', 'c'), ('b', 'c')])
        self.assertEqual(uw_graph.get_neighbors('a'), ['b', 'c'])
        self.assertEqual(uw_graph.get_neighbors('b'), ['c'])

    def test_undirected_weighted_graph(self):
        weighted_graph = WeightedGraph(is_directed=False)
        weighted_graph.add_vertex('a')
        weighted_graph.add_vertex('b')
        weighted_graph.add_vertex('c')
        weighted_graph.add_vertex('d')
        self.assertFalse(weighted_graph.is_directed())
        self.assertEqual(weighted_graph.get_vertices(), ['a', 'b', 'c', 'd'])
        weighted_graph.add_edge('a', 'c')
        weighted_graph.add_edge('a', 'b', 100)
        self.assertEqual(weighted_graph.get_vertex('a').get_key(), 'a')
        self.assertEqual(weighted_graph.get_neighbors('a'), ['c', 'b'])
        self.assertEqual(weighted_graph.get_neighbors('b'), ['a'])
        self.assertEqual(weighted_graph.get_weight('a', 'c'), 0)
        self.assertEqual(weighted_graph.get_weight('a', 'b'), 100)
        self.assertEqual(weighted_graph.get_weight('b', 'a'), 100)
    
    def test_directed_weighted_graph(self):
        weighted_graph = WeightedGraph(is_directed=True)
        weighted_graph.add_vertex('a')
        weighted_graph.add_vertex('b')
        weighted_graph.add_vertex('c')
        self.assertTrue(weighted_graph.is_directed())
        self.assertEqual(weighted_graph.get_vertices(), ['a', 'b', 'c'])
        weighted_graph.add_edge('a', 'c')
        weighted_graph.add_edge('a', 'b', 100)
        self.assertEqual(weighted_graph.get_vertex('a').get_key(), 'a')
        self.assertEqual(weighted_graph.get_neighbors('a'), ['c', 'b'])
        self.assertEqual(weighted_graph.get_neighbors('b'), [])
        self.assertEqual(weighted_graph.get_weight('a', 'c'), 0)
        self.assertEqual(weighted_graph.get_weight('a', 'b'), 100)
        self.assertIsNone(weighted_graph.get_weight('b', 'a'))