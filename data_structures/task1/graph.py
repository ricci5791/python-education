"""Graph implementation with linked-list"""
from typing import Optional

from data_structures.task1.mylinkedlist import LinkedList


class Graph:
    """Graph"""

    class Vertex:
        """Class with node implementation"""

        def __init__(self, value):
            self.value = value
            self.adj_nodes = LinkedList()

        def add_edge(self, node):
            """
            Add edge to the given node

            :param node: Node itself
            :return: None
            """
            self.adj_nodes.append(node)
            node.adj_nodes.append(self)

        def delete_edge(self, node):
            """
            Deletes references for the given node

            :param node: Value of the vertex to be deleted
            :return:
            """
            index = self.adj_nodes.lookup(node)
            if index == -1:
                return

            self.adj_nodes.delete(index)

        def __str__(self):
            return f"V:{self.value}"

    def __init__(self):
        self.nodes_list = LinkedList()

    def insert(self, node_value, adj_list: list) -> None:
        """
        Inserts new vertex with given value

        :param node_value: Value to be inserted in the new node
        :param adj_list: List of edges between vertices(if doesn't exists
        created in place)
        :return: None
        """
        new_node = Graph.Vertex(node_value)

        for item in adj_list:
            node = self.lookup(item)

            if node is None:
                node = Graph.Vertex(item)
            new_node.add_edge(node)

        self.nodes_list.append(new_node)

    def lookup(self, value) -> Optional[Vertex]:
        """
        Return reference of the node with given value

        :param value: Value of the node
        :return: Reference of the node, None if wasn't found
        """
        for node in self:
            if node.value == value:
                return node
        return None

    def delete(self, deletion_node) -> None:
        """
        Delete node with given reference of it

        :param deletion_node: Vertex to be deleted
        :return: None
        """
        if deletion_node is None:
            return
        adj_nodes = deletion_node.adj_nodes

        for node in adj_nodes:
            node.value.delete_edge(deletion_node)

        self.nodes_list.delete(self.nodes_list.lookup(deletion_node))

    def print(self):
        """
        Prints vertex and its connected neighbors

        :return: None
        """
        for node in self:
            print(node.value)
            print("Adjacent to " + str(node.adj_nodes))

    def __str__(self):
        return f"{self.nodes_list}"

    def __iter__(self):
        nodes_list = self.nodes_list

        for node in nodes_list:
            yield node.value
