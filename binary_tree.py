class Node:
    """
    Node object used to build various tree objects

    Attributes
    ----------
    key : anything
        variable used in comparison when building trees
    value : anything (optional)
        variable stored value, if not supplied uses key
    left : Node
        left connection to this node
    right : Node
        right connection to this node
    """

    def __init__(self, key, value=None, left=None, right=None):
        """
        constructor for Node object

        Arguments
        ---------
        key : anything
            variable used in comparison when building trees
        value : anything (optional)
            variable stored value, if not supplied uses key
        left : Node
            left connection to this node
        right : Node
            right connection to this node
        """
        if left is not None:
            if not isinstance(left, Node):
                raise TypeError("Node: left children must be Node object!")
        if right is not None:
            if not isinstance(right, Node):
                raise TypeError("Node: right children must be Node object!")
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.value is None:
            self.value = key


class BinaryTree:
    """
    implementation of a binary tree

    Attributes
    ----------
    tree : Node
        intenal storage of tree object

    Methods
    -------
    insert(key, value = None, node = None)
        insert new nodes to the binary tree
    search(key, value = None, node = None)
        search the binary tree for values
    """

    def __init__(self, keys=None, values=None):
        """
        constructor for BinaryTree object

        Arguments
        ---------
        keys : list
            list of keys used in binary tree
        values : list
            list of values used to be matched with supplied keys
        """
        self.tree = None
        if keys:
            if values is None:
                values = keys
            if not isinstance(keys, list) and not isinstance(values, list):
                raise TypeError(
                    "BinaryTree: keys and values inputs must be lists!")
            if len(values) != len(keys):
                raise IndexError(
                    "BinaryTree: input keys and values list " +
                    "must be the same length!")
            for key, value in zip(keys, values):
                self.insert(key, value)

    def insert(self, key, value=None, node=None):
        """
        insert keys/values into binary tree

        Arguments
        ---------
        key : anything
            variable used for traveling through the tree
        value : anything
            variable stored at the given key site
        node : Node
            node to insert value, primarily used in recursion
        """
        if self.tree is None:
            self.tree = Node(key, value=value)
            self.type = type(key)
        else:
            if node is None:
                node = self.tree
            try:
                if key < node.key:
                    if node.left is None:
                        node.left = Node(key, value=value)
                    else:
                        self.insert(key, value=value, node=node.left)
                else:
                    if node.right is None:
                        node.right = Node(key, value=value)
                    else:
                        self.insert(key, value=value, node=node.right)
            except TypeError:
                raise TypeError("BinaryTree: Cannot compare types, " +
                                str(type(key) + " with " +
                                    str(type(node.key))))

    def search(self, key, node=None):
        """
        search keys/value pairs within BinaryTree object

        Arguments
        ---------
        key : anything
            variable used for traveling through the tree
        node : Node
            node to search for key, primarily used in recursion
        """
        if self.tree is None:
            return -1
        else:
            if node is None:
                node = self.tree
            try:
                key > node.key
            except TypeError:
                raise TypeError("BinaryTree: Cannot compare types, " +
                                str(type(key) + " with " +
                                    str(type(node.key))))
            if key < node.key:
                if node.left is None:
                    return -1
                else:
                    return self.search(key, node=node.left)
            if key > node.key:
                if node.right is None:
                    return -1
                else:
                    return self.search(key, node=node.right)
            if key == node.key:
                return node.value
