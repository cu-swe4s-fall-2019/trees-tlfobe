import unittest
import gen_data


class TestRandomGenerators(unittest.TestCase):
    def test_random_string(self):
        assert type(gen_data.random_string()) == str

    def test_random_float(self):
        assert type(gen_data.random_float()) == float

    def test_random_int(self):
        assert type(gen_data.random_int()) == int
