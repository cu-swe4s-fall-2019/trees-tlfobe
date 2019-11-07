import unittest
import binary_tree


class TestNode(unittest.TestCase):
    def test_single_node(self):
        node = binary_tree.Node(10)
        assert node.key == 10
        assert node.left is None
        assert node.right is None
        assert node.value == 10

    def test_single_node_hash(self):
        node = binary_tree.Node(10, 'string!')
        assert node.key == 10
        assert node.left is None
        assert node.right is None
        assert node.value == 'string!'

    def test_node_incorrect_child(self):
        self.assertRaises(TypeError, binary_tree.Node,
                          10, 10, left=10, right=20)

    def test_node_correct_child(self):
        left_child = binary_tree.Node(4)
        right_child = binary_tree.Node(16)
        node = binary_tree.Node(10, left=left_child, right=right_child)
        assert node.left.key == 4
        assert node.right.key == 16


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree_incorrect_input(self):
        self.assertRaises(TypeError, binary_tree.BinaryTree, keys = 'string!', values = 100)

    def test_binary_tree_init_incorrect_lists(self):
        self.assertRaises(IndexError, binary_tree.BinaryTree, keys = [1,2,3,4], values = ['a', 'b','c'])

    def test_binary_tree_init_no_in(self):
        bt = binary_tree.BinaryTree()
        assert bt.tree is None

    def test_binary_tree_init_values(self):
        bt = binary_tree.BinaryTree(keys = [1,2,3,4,0])
        assert bt.tree.value == 1
        assert bt.tree.right.value == 2
        assert bt.tree.right.right.value == 3
        assert bt.tree.right.right.right.value == 4
        assert bt.tree.left.value == 0

    def test_binary_tree_wrong_types(self):
        bt = binary_tree.BinaryTree(keys = [1,2,3,4,0])
        self.assertRaises(TypeError, bt.insert, 'string')

    def test_binary_tree_insert(self):
        bt = binary_tree.BinaryTree()
        bt.insert(10)
        bt.insert(11)
        bt.insert(9)
        assert bt.tree.left.value == 9
        assert bt.tree.right.value == 11
    
    def test_binary_tree_init_key_value(self):
        bt = binary_tree.BinaryTree(keys = [1,2,3,4,0], values=['one', 'two', 'three', 'four', 'zero'])
        assert bt.tree.key == 1
        assert bt.tree.right.key == 2
        assert bt.tree.right.right.key == 3
        assert bt.tree.right.right.right.key == 4
        assert bt.tree.left.key == 0
        assert bt.tree.value == 'one'
        assert bt.tree.right.value == 'two'
        assert bt.tree.right.right.value == 'three'
        assert bt.tree.right.right.right.value == 'four'
        assert bt.tree.left.value == 'zero'

    def test_binary_tree_search(self):
        bt = binary_tree.BinaryTree(keys = [1,2,3,4,0], values=['one', 'two', 'three', 'four', 'zero'])
        assert bt.search(1) == 'one'
        assert bt.search(2) == 'two'
        assert bt.search(3) == 'three'
        assert bt.search(4) == 'four'
        assert bt.search(0) == 'zero'

    def test_binary_tree_search_no_find(self):
        bt = binary_tree.BinaryTree(keys = [1,2,3,4,0], values=['one', 'two', 'three', 'four', 'zero'])
        assert bt.search(11) == -1
        assert bt.search(100) == -1
        bt.insert(11, value='eleven')
        bt.insert(100, value='hundred')
        assert bt.search(11) == 'eleven'
        assert bt.search(100) == 'hundred'

    def test_binary_tree_mixed_key_value_no_value(self):
        bt = binary_tree.BinaryTree(keys = [1,2,3,4,0], values=['one', 'two', 'three', 'four', 'zero'])
        bt.insert(23)
        assert bt.search(23) == 23
        assert bt.search(1) == 'one'


