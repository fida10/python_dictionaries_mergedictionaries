import unittest
from src.ans import merge_dictionaries


class TestMergeDictionaries(unittest.TestCase):
    def test_merge_dictionaries(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_merge_with_empty_dictionary(self):
        self.assertEqual(merge_dictionaries(
            {'a': 1, 'b': 2}, {}), {'a': 1, 'b': 2})

    def test_both_dictionaries_empty(self):
        self.assertEqual(merge_dictionaries({}, {}), {})


if __name__ == '__main__':
    unittest.main()
