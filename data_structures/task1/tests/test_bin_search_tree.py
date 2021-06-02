"""Module with binary search tree tests"""
import pytest

from data_structures.task1.binary_search_tree import BinSearchTree as Tree


@pytest.fixture(name="bin_tree")
def fixture_single_root_bin_tree():
    """
    Mocks binary tree with root value of 8
    :return:
    """
    return Tree(8)


@pytest.fixture(name="filled_bin_tree")
def fixture_filled_bin_tree():
    """
    Mocks filled binary search tree with root 8
    :return:
    """
    tree = Tree(8)

    for item in [5, 2, 6, 7, 10, 14]:
        tree.insert(item)

    return tree


@pytest.mark.parametrize("test_values, expected_traversal", [
    ([2, 5, 6, 7, 10, 14], "2 5 6 7 8 10 14"),
    ([2, 5, 6, 7, 10, 14, 11], "2 5 6 7 8 10 11 14"),
    ([10, 11, 50], "8 10 11 50"),
    ([8, 8, 8], "8 8 8 8"),
    ([2, 1, 0, -1, -2], "-2 -1 0 1 2 8"),
])
def test_bin_tree_insert(bin_tree, test_values, expected_traversal):
    for test_item in test_values:
        bin_tree.insert(test_item)
    assert bin_tree.inorder_traversal() == expected_traversal


@pytest.mark.parametrize("value, expected_leaves_value", [
    (5, (2, 6)),
    (8, (5, 10)),
    (8, (5, 10)),
])
def test_bin_tree_lookup_nodes(filled_bin_tree, value, expected_leaves_value):
    node = filled_bin_tree.lookup(value)

    left, right = expected_leaves_value

    assert node.left.value == left and node.right.value == right


@pytest.mark.parametrize("value", [2, 14, 7])
def test_bin_tree_lookup_leaves(filled_bin_tree, value):
    node = filled_bin_tree.lookup(value)

    assert node.left is None and node.right is None


@pytest.mark.parametrize("test_value", [7, 9, 2, 5, 6])
def test_bin_tree_delete(filled_bin_tree, test_value):
    filled_bin_tree.delete(test_value)
    assert filled_bin_tree.lookup(test_value) is None
