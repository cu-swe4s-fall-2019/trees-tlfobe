import unittest
import os
import insert_key_value_pairs


class TestGetKeyValuePairsFromFile(unittest.TestCase):
    def setUp(self):
        os.system(
            "python gen_data.py --key_type string --value_type int " +
            "--outfile test.txt")
        with open("test2.txt", "w") as fh:
            fh.write("1 2 3")
            fh.write("1 2 3")
            fh.write("1 2 3")

    def test_read_file(self):
        keys, values = insert_key_value_pairs.get_key_value_pairs_from_file(
            "test.txt", 10000)
        assert len(keys) == 10000
        assert len(values) == 10000

    def test_get_key_value_pair_from_file_invalid_file(self):
        self.assertRaises(
            FileNotFoundError,
            insert_key_value_pairs.get_key_value_pairs_from_file,
            "not_file.txt", 10000)

    def test_get_key_value_pair_from_file_dir(self):
        self.assertRaises(
            FileNotFoundError,
            insert_key_value_pairs.get_key_value_pairs_from_file,
            "avl_tree", 10000)

    def test_get_key_value_pair_from_file_bad_format(self):
        self.assertRaises(
            IOError,
            insert_key_value_pairs.get_key_value_pairs_from_file,
            "test2.txt", 3)

    def test_get_n_key_value_pair_from_file(self):
        keys, values = insert_key_value_pairs.get_key_value_pairs_from_file(
            "test.txt", 40)
        assert len(keys) == 40
        assert len(values) == 40


    def tearDown(self):
        os.remove('test.txt')
        os.remove('test2.txt')
