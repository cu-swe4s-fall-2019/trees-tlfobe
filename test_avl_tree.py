import avl_tree
import unittest


class TestAVLNode(unittest.TestCase):
    def test_single_node(self):
        node = avl_tree.AVLNode(10)
        assert node.key == 10
        assert node.left is None
        assert node.right is None
        assert node.value == 10

    def test_single_node_hash(self):
        node = avl_tree.AVLNode(10, 'string!')
        assert node.key == 10
        assert node.left is None
        assert node.right is None
        assert node.value == 'string!'

    def test_node_incorrect_child(self):
        self.assertRaises(TypeError, avl_tree.AVLNode,
                          10, 10, left=10, right=20)

    def test_node_correct_child(self):
        left_child = avl_tree.AVLNode(4)
        right_child = avl_tree.AVLNode(16)
        node = avl_tree.AVLNode(10, left=left_child, right=right_child)
        assert node.left.key == 4
        assert node.right.key == 16


class TestAVLTree(unittest.TestCase):
    def test_avl_tree_incorrect_input(self):
        self.assertRaises(TypeError, avl_tree.AVLTree,
                          keys='string!', values=100)

    def test_avl_tree_init_incorrect_lists(self):
        self.assertRaises(IndexError, avl_tree.AVLTree, keys=[
                          1, 2, 3, 4], values=['a', 'b', 'c'])

    def test_avl_tree_init_no_in(self):
        bt = avl_tree.AVLTree()
        assert bt.tree is None

    def test_avl_tree_init_values(self):
        bt = avl_tree.AVLTree(keys=[1, 2, 3, 4, 0])
        assert bt.tree.value == 2
        assert bt.tree.right.value == 3
        assert bt.tree.right.right.value == 4
        assert bt.tree.left.value == 1
        assert bt.tree.left.left.value == 0

    def test_avl_tree_wrong_types(self):
        bt = avl_tree.AVLTree(keys=[1, 2, 3, 4, 0])
        self.assertRaises(TypeError, bt.insert, 'string')

    def test_avl_tree_insert(self):
        bt = avl_tree.AVLTree()
        bt.insert(10)
        bt.insert(11)
        bt.insert(9)
        assert bt.tree.left.value == 9
        assert bt.tree.right.value == 11

    def test_avl_tree_init_key_value(self):
        bt = avl_tree.AVLTree(keys=[1, 2, 3, 4, 0], values=[
            'one', 'two', 'three', 'four', 'zero'])
        assert bt.tree.key == 2
        assert bt.tree.right.key == 3
        assert bt.tree.right.right.key == 4
        assert bt.tree.left.key == 1
        assert bt.tree.left.left.key == 0
        assert bt.tree.value == "two"
        assert bt.tree.right.value == "three"
        assert bt.tree.right.right.value == "four"
        assert bt.tree.left.value == "one"
        assert bt.tree.left.left.value == "zero"

    def test_avl_tree_search(self):
        bt = avl_tree.AVLTree(keys=[1, 2, 3, 4, 0], values=[
            'one', 'two', 'three', 'four', 'zero'])
        assert bt.search(1) == 'one'
        assert bt.search(2) == 'two'
        assert bt.search(3) == 'three'
        assert bt.search(4) == 'four'
        assert bt.search(0) == 'zero'

    def test_avl_tree_search_no_find(self):
        bt = avl_tree.AVLTree(keys=[1, 2, 3, 4, 0], values=[
            'one', 'two', 'three', 'four', 'zero'])
        assert bt.search(11) == -1
        assert bt.search(100) == -1
        bt.insert(11, value='eleven')
        bt.insert(100, value='hundred')
        assert bt.search(11) == 'eleven'
        assert bt.search(100) == 'hundred'

    def test_avl_tree_mixed_key_value_no_value(self):
        bt = avl_tree.AVLTree(keys=[1, 2, 3, 4, 0], values=[
            'one', 'two', 'three', 'four', 'zero'])
        bt.insert(23)
        assert bt.search(23) == 23
        assert bt.search(1) == 'one'

    def test_avl_tree_left_rotate(self):
        avl = avl_tree.AVLTree([1, 2, 3, 4, 5])
        assert avl.tree.value == 2
        assert avl.tree.left.value == 1
        assert avl.tree.right.value == 4
        assert avl.tree.right.left.value == 3
        assert avl.tree.right.right.value == 5

    def test_avl_tree_right_rotate(self):
        avl = avl_tree.AVLTree([5, 4, 3, 2, 1])
        assert avl.tree.value == 4
        assert avl.tree.left.value == 2
        assert avl.tree.right.value == 5
        assert avl.tree.left.left.value == 1
        assert avl.tree.left.right.value == 3

    def test_avl_tree_test_right_left_rotation(self):
        avl = avl_tree.AVLTree([5, 8, 6])
        assert avl.tree.value == 6
        assert avl.tree.right.value == 8
        assert avl.tree.left.value == 5

    def test_avl_tree_test_left_right_rotation(self):
        avl = avl_tree.AVLTree([8, 5, 6])
        assert avl.tree.value == 6
        assert avl.tree.right.value == 8
        assert avl.tree.left.value == 5
