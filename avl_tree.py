from binary_tree import Node
from binary_tree import BinaryTree

class AVLNode(Node):
    """
    AVL Node for building an AVL tree
    """
    def __init__(self, key, value=None, left=None, right=None):
        Node.__init__(self, key, value=None, left=None, right=None)
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
    balance_tree   
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
                    if node.left is None:
                        node.left = AVLNode(key, value=value)
                    else:
                        self.insert(key, value=value, node=node.left, parent=node)
                else:
                    if node.right is None:
                        node.right = AVLNode(key, value=value)
                    else:
                        self.insert(key, value=value, node=node.right, parent=node)
                node.height += 1
                if node.left == None:
                    left_height = -1
                else:
                    left_height = node.left.height
                if node.right == None:
                    right_height = -1
                else:
                    right_height = node.right.height
                node.balance_factor= abs(left_height - right_height)
                if node.balance_factor > 1:
                    self.balance_tree(node, parent)
            except TypeError:
                raise TypeError("BinaryTree: Cannot compare types, " +
                                str(type(key) + " with " +
                                    str(type(node.key))))
    def balance_tree(self, node, parent):
        left_height = -1 if node.left == None else node.left.height
        right_height = -1 if node.right == None else node.right.height
        
        if left_height > right_height:
            left_height = -1 if node.left.left == None else node.left.left.height
            right_height = -1 if node.left.right == None else node.left.right.height
            if left_height > right_height:
                # Left Left --> Right rotate
                self.right_rotate(parent)
            else:
                # Left Right
                self.left_rotate(node)
                self.right_rotate(parent)
        else:
            left_height = -1 if node.right.left == None else node.right.left.height
            right_height = -1 if node.right.right == None else node.right.right.height
            if left_height > right_height:
                # Right Left
                self.right_rotate(node)
                self.left_rotate(parent)
            else:
                # Right Right
                self.left_rotate(parent)
        

            

    def right_rotate(self, node):
        print("Rotating Right!")
        reconsile = node.left
        new_root = node.left
        new_root.right = node
        new_root.right.left = reconsile
        return new_root

        
    def left_rotate(self, node):
        print("Rotating Left!")
        reconsile = node.right.left
        new_root = node.right
        new_root.left = node
        new_root.left.right = reconsile
        return new_root

    