from dijkstra import Graph
import unittest

class TestShortestPath(unittest.TestCase):
    def setUp(self):
        # Create a graph instance for testing
        self.graph = Graph()

    def test_shortest_path_simple(self):
        # Test a simple graph with a clear shortest path
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('A', 'C', 4)
        self.graph.add_edge('C', 'C', 0)
        self.assertEqual(self.graph.shortest_path('A', 'C'), ['A', 'B', 'C'])

    def test_no_path_exists(self):
        # Test a graph where no path exists between source and target
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('C', 'D', 2)
        self.graph.add_edge('D', 'D', 0)
        self.assertEqual(self.graph.shortest_path('D', 'A'), [])

    def test_multiple_paths(self):
        # Test a graph with multiple paths to the target
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('C', 'A', 4)
        self.graph.add_edge('A', 'D', 3)
        self.graph.add_edge('D', 'C', 1)
        self.assertEqual(self.graph.shortest_path('A', 'C'), ['A', 'B', 'C'])

    def test_large_graph(self):
        # Test a larger graph with multiple nodes and edges
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('C', 'D', 3)
        self.graph.add_edge('D', 'E', 4)
        self.graph.add_edge('E', 'A', 10)
        self.assertEqual(self.graph.shortest_path('A', 'E'), ['A', 'B', 'C', 'D', 'E'])

    def test_graph_with_cycles(self):
        # Test a graph with cycles
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('B', 'C', 2)
        self.graph.add_edge('C', 'A', 3)
        self.graph.add_edge('C', 'D', 4)
        self.graph.add_edge('D', 'D', 0)
        self.assertEqual(self.graph.shortest_path('A', 'D'), ['A', 'B', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
