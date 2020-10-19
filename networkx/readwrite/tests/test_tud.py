"""
    Unit tests for TUD.
"""
import tempfile
import networkx as nx


class TestTud:
    @classmethod
    def setup_class(cls):
        cls.graphs = []

        g1 = nx.Graph(name="test")
        e = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("a", "f")]
        g1.add_edges_from(e)
        cls.graphs.append(g1)

        g2 = nx.Graph(name="test")
        g2.add_edges_from(e)
        cls.graphs.append(g2)

    def test_one(self):
        p = tempfile.mkdtemp()
        nx.write_tud(self.graphs, path=p)

        adj_matrix_file = p + "/DS_A.txt"
        assert sum(1 for _ in open(adj_matrix_file)) == 2 * 2 * 6
