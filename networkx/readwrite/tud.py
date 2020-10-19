"""Functions for reading and writing graph datasets in TUDataset format


For more information, see the `TUDataset`_ website.

.. _TUdataset: https://chrsmrrs.github.io/datasets/docs/format/

"""
import networkx as nx
from networkx.exception import NetworkXError
from networkx.utils import open_file, not_implemented_for

__all__ = []
