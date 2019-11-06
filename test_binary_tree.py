import unittest
import binary_tree

class TestNode(unittest.TestCase):
    def test_single_node(self):
        node = binary_tree.Node(10)
        assert node.key == 10
        assert node.left is None
        assert node.right is None

    def test_incorrect_child(self):
        self.assertRaises(TypeError, binary_tree.Node, 10, 10, left=10, right=20)

    def test_correct_child(self):
        left_child = binary_tree.Node(4)
        right_child = binary_tree.Node(16)
        node = binary_tree.Node(10, left=left_child, right=right_child)
        assert node.left.key == 4
        assert node.right.key == 16
        

