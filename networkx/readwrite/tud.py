"""Functions for reading and writing graph datasets in TUDataset format


For more information, see the `TUDataset`_ website.

.. _TUdataset: https://chrsmrrs.github.io/datasets/docs/format/

"""
import networkx as nx
from networkx.exception import NetworkXError
from networkx.utils import open_file, not_implemented_for

__all__ = ["write_tud"]


def write_tud(graphs, path, name="DS", encoding="utf-8"):
    """Save a collection of graphs in TUDataset format.

        Parameters
        ----------
        graphs : NetworkX graphs
            Iterator or iterable collection of graphs

        path : string or file
           Filename of directory to store files in

        name : string
           Name for the dataset

        encoding : string, optional
           Text encoding.
    """
    # merged graphs
    adjacency_matrix_file = f"{path}/{name}_A.txt"
    graph_indicator_file = f"{path}/{name}_graph_indicator.txt"

    # labels#
    graph_labels_file = f"{path}/{name}_graph_labels.txt"
    node_labels_file = f"{path}/{name}_node_labels.txt"
    edge_labels_file = f"{path}/{name}_edge_labels.txt"

    # attributes
    graph_attributes_file = f"{path}/{name}_graph_attributes.txt"
    node_attributes_file = f"{path}/{name}_node_attributes.txt"
    edge_attributes_file = f"{path}/{name}_edge_attributes.txt"

    num_graphs_seen = 0
    num_nodes_seen = 0
    num_edges_seen = 0
    with open(adjacency_matrix_file, 'w', encoding=encoding) as amf, \
            open(graph_indicator_file, 'w', encoding=encoding) as gif, \
            open(graph_attributes_file, 'w', encoding=encoding) as gaf, \
            open(node_attributes_file, 'w', encoding=encoding) as naf, \
            open(edge_attributes_file, 'w', encoding=encoding) as eaf:

        for i, og in enumerate(graphs):
            assert not og.is_directed()
            g = og.copy()
            # graph
            g = nx.convert_node_labels_to_integers(g, first_label=num_nodes_seen)
            num_graphs_seen += 1

            # nodes
            for j in range(num_nodes_seen, num_nodes_seen + g.number_of_nodes()):
                gif.write(f"{i}\n")
                naf.write(", ".join(str(v) for v in g.nodes[j].values()) + '\n')

            num_nodes_seen += g.number_of_nodes()

            # edges
            for u, v, d in g.edges(data=True):
                amf.write(f"{u} {v}\n")
                amf.write(f"{v} {u}\n")
                num_edges_seen += 1
