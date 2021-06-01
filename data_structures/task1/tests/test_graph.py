"""Module with graph tests"""
import pytest

from data_structures.task1.graph import Graph


@pytest.fixture(name="empty_graph")
def fixture_empty_graph():
    """
    Mocks empty graph
    """
    return Graph()


@pytest.fixture(name="filled_graph")
def fixture_filled_graph():
    """
    Mocks graph with vertices and edges
    """
    graph = Graph()
    graph.insert(1, [2, 4])
    graph.insert(2, [1, 3, 5])

    return graph


@pytest.mark.parametrize("test_node, test_edges, expected", [
    (1, [], []),
    (2, [1], [2]),
    (3, [2], [3]),
    (4, [1], [4]),
    (5, [2, 3], [5]),
])
def test_graph_insert(empty_graph, test_node, test_edges, expected):
    empty_graph.insert(test_node, test_edges)
    for vertex in empty_graph.lookup(test_node).adj_nodes:
        assert vertex.value.adj_nodes == expected


@pytest.mark.parametrize("test_node_value_list", [[1, 2, 3, 4, 5, 6]])
def test_graph_full_delete(filled_graph, test_node_value_list):
    for test_value in test_node_value_list:
        node = filled_graph.lookup(test_value)
        filled_graph.delete(node)

    assert filled_graph.nodes_list == []
