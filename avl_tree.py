from binary_tree import BinaryTree


class AVLNode():
    """
    AVL Node for building an AVL tree
    """

    def __init__(self, key, value=None, left=None, right=None):
        if left is not None:
            if not isinstance(left, AVLNode):
                raise TypeError("Node: left children must be Node object!")
        if right is not None:
            if not isinstance(right, AVLNode):
                raise TypeError("Node: right children must be Node object!")
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.value is None:
            self.value = key
        self.height = 0
        self.balance_factor = 0


class AVLTree(BinaryTree):
    """
    implementation of an AVL tree

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
    left_rotation(node)
        peform a left rotation on a node
    right_toration(node)
        perform a right rotation on a node
    left_right_rotation(node)
        perform a left_right rotation on a node
    right_left_rotation(node)
        perform a right_left rotation on a node
    balance_tree(self, node)
        perform a balance to a node with balance factor over 1
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

    def insert(self, key, value=None, node=None, parent=None):
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
            self.tree = AVLNode(key, value=value)
            self.type = type(key)
        else:
            if node is None:
                node = self.tree
            try:
                if key < node.key:
                    direct = "left"
                    if node.left is None:
                        node.left = AVLNode(key, value=value)
                    else:
                        self.insert(key, value=value,
                                    node=node.left, parent=node)
                else:
                    direct = "right"
                    if node.right is None:
                        node.right = AVLNode(key, value=value)
                    else:
                        self.insert(key, value=value,
                                    node=node.right, parent=node)
                node.height += 1
                node.balance_factor = self.calc_balance_factor(node)
                if node.balance_factor > 1:
                    node = self.balance_tree(node)
                    if parent is not None:
                        parent.height -= 1
                        if direct == "left":
                            parent.left = node
                        elif direct == "right":
                            parent.right = node
                        else:
                            print("you shouldn't be here!")
                    else:
                        self.tree = node

            except TypeError:
                raise TypeError("BinaryTree: Cannot compare types, " +
                                str(type(key) + " with " +
                                    str(type(node.key))))

    def calc_balance_factor(self, node):
        """
        internal function used for calculating balance factors

        Arguments
        ---------
        node : AVLNode
            node to calculate balance factor for

        Returns
        -------
        balance_factor : int
            value used to determine rebalancing tree
        """
        if node.left is None:
            left_height = -1
        else:
            left_height = node.left.height
        if node.right is None:
            right_height = -1
        else:
            right_height = node.right.height
        return abs(left_height - right_height)

    def balance_tree(self, node):
        """
        function for selecting which type of rotation to perform on node

        Arguments
        ---------
        node : AVLNode
            node to perform balancing on
        """
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height

        if left_height > right_height:
            left_height = \
                -1 if node.left.left is None else node.left.left.height
            right_height = \
                -1 if node.left.right is None else node.left.right.height
            if left_height > right_height:
                # Left Left --> Right rotate
                node = self.right_rotate(node)
            else:
                # Left Right
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
                node.height += 1
                node.left.height += 1
        else:
            left_height = \
                -1 if node.right.left is None else node.right.left.height
            right_height = \
                -1 if node.right.right is None else node.right.right.height
            if left_height > right_height:
                # Right Left
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
                node.height += 1
                node.right.height += 1
            else:
                # Right Right
                node = self.left_rotate(node)
        return(node)

    def right_rotate(self, node):
        """
        rotate a node to the right

        Arguments
        ---------
        node : AVLNode
            node to perform rotation on
        """
        # print("Rotating Right!")
        reconsile = node.left.right
        new_root = node.left
        new_root.right = node
        if reconsile is None:
            new_root.right.height -= 2
        else:
            new_root.right.height -= 1
        new_root.right.left = reconsile
        new_root.balance_factor = self.calc_balance_factor(new_root)
        if new_root.left is not None:
            new_root.left.balance_factor = self.calc_balance_factor(
                new_root.left)
        if new_root.right is not None:
            new_root.right.balance_factor = self.calc_balance_factor(
                new_root.right)
        return new_root

    def left_rotate(self, node):
        """
        rotate a node to the right

        Arguments
        ---------
        node : AVLNode
            node to perform rotation on
        """
        # print("Rotating Left!")
        reconsile = node.right.left
        new_root = node.right
        new_root.left = node
        if reconsile is None:
            new_root.left.height -= 2
        else:
            new_root.left.height -= 1
        new_root.left.right = reconsile
        new_root.balance_factor = self.calc_balance_factor(new_root)
        if new_root.left is not None:
            new_root.left.balance_factor = self.calc_balance_factor(
                new_root.left)
        if new_root.right is not None:
            new_root.right.balance_factor = self.calc_balance_factor(
                new_root.right)
        return new_root
