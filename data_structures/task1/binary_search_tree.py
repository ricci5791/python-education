"""Module contains binary search tree implementation"""


class BinSearchTree:
    """Binary search tree implementation"""

    class Node:
        """
        Basic node of tree implementation
        """

        def __init__(self, value, parent):
            self.value = value
            self.parent = parent
            self.left = None
            self.right = None

        def _insert_left(self, value):
            """
            Inserts to the left node of the tree

            :param value: Data to be stored
            :return: new node
            """
            self.left = BinSearchTree.Node(value, self)
            return self.left

        def _insert_right(self, value):
            """
            Inserts to the right node of the tree

            :param value: Data to be stored
            :return: new node
            """
            self.right = BinSearchTree.Node(value, self)
            return self.right

        def __str__(self):
            return f"{self.value}, r:({self.right}), l:({self.left})"

    def __init__(self, value):
        self.root = BinSearchTree.Node(value, None)
        self.inorder_traversal_str = ""

    def insert(self, value):
        """
        Inserts data to the tree

        :param value: Data to be stored
        :return: None
        """
        curr_node = self.root

        while True:
            if value >= curr_node.value:
                if curr_node.right is None:
                    curr_node.right = BinSearchTree.Node(value, curr_node)
                    break
                curr_node = curr_node.right
            else:
                if curr_node.left is None:
                    curr_node.left = BinSearchTree.Node(value, curr_node)
                    break
                curr_node = curr_node.left

    def lookup(self, value):
        """
        Return reference for the element with the given value

        :param value: Value to be searched
        :return: Reference if exists
        """
        curr_node = self.root

        while True:
            if curr_node is None:
                break

            if curr_node.value == value:
                return curr_node
            if value >= curr_node.value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

    def delete(self, value):
        """
        Delete node with given value and can be replaced with leaves if exist

        :param value: Value to be looked for
        :return: None
        """
        curr_node = self.lookup(value)
        if curr_node is None:
            return
        prev_node = curr_node.parent

        if curr_node.left is None:
            if curr_node.right is None:
                if prev_node.left is curr_node:
                    prev_node.left = None
                else:
                    prev_node.right = None
            else:
                curr_node.value = curr_node.right.value
                curr_node.right = None
        else:
            iter_node = curr_node.left
            prev_node = iter_node
            while iter_node.right is not None:
                iter_node = iter_node.right
            prev_node.right = None
            curr_node.value = iter_node.value

    def inorder_traversal(self):
        """
        Makes inorder traversal through the tree

        :return:
        """
        self.inorder_traversal_str = ""

        self._inorder_traversal(self.root)
        return self.inorder_traversal_str.strip()

    def _inorder_traversal(self, node):
        if node.left is not None:
            self._inorder_traversal(node.left)
        self.inorder_traversal_str += " " + str(node.value)
        if node.right is not None:
            self._inorder_traversal(node.right)
