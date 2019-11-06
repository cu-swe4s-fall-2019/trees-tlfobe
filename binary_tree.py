class Node:
    def __init__(self, key, value=None, left=None, right=None):
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


def insert(root, key, value=None):
    return root


def search(root, key):
    return None
